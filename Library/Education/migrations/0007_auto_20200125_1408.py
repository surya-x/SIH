# Generated by Django 3.0.1 on 2020-01-25 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Education', '0006_auto_20200125_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='books_issued',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]