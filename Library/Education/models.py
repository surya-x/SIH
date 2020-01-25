from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator, RegexValidator

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length = 100)
    pic = models.ImageField(upload_to = "images", null=True)
    genre = models.CharField(max_length=20, default="Not provided", choices=(("story","story"), ("autobiography","autobiography"), ("inspirational","inspirational")))
    description = models.TextField(null=True, blank=True)
    pages = models.CharField(max_length = 5)
    author = models.CharField(max_length = 100)
    aboutAuthor = models.CharField(max_length = 500, blank=True, null=True)
    copies = models.IntegerField(default=1, null=True, blank=True)
    rack_no = models.IntegerField( null=True, blank=True)
    def __str__(self):
        return "%s" % self.title

class Dashboard(models.Model):
    name = models.CharField(max_length = 100)
    user = models.OneToOneField(to=User, on_delete=CASCADE)
    age = models.IntegerField(default=18, validators=[MinValueValidator(18)])
    programme = models.CharField(max_length = 100)
    pic = models.ImageField(upload_to = "images", null=True, blank=True)
    books_issued = models.IntegerField(default=0, null=True, blank=True)

class BookIssue(models.Model):
    book_id = models.ForeignKey(to=Book, on_delete=CASCADE)
    user = models.OneToOneField(to=User, on_delete=CASCADE)
    requrest_issue = models.CharField(max_length=20, default="Reject", choices=(("Accept","Accept"), ("Reject","Reject")))
