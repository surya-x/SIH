from django.contrib import admin
from Education.models import Book, Dashboard, BookIssue
from django.contrib.admin.options import ModelAdmin

admin.site.site_header = 'Dr. B.R. Ambedkar Institute of Technology'

class BookAdmin(ModelAdmin):
    list_display = ["title", "author", "genre"]
    search_fields = ["title", "author", "genre"]
    list_filter = ["title", "author", "genre"]
admin.site.register(Book, BookAdmin)


class DashboardAdmin(ModelAdmin):
    list_display = ["name", "age", "programme"]
    search_fields = ["name", "age", "programme"]
    list_filter = ["name", "age", "programme"]
admin.site.register(Dashboard, DashboardAdmin)


class BookIssueAdmin(ModelAdmin):
    list_display = ["book_id", "user"]
    search_fields = ["book_id", "user"]
    list_filter = ["book_id", "user"]
admin.site.register(BookIssue, BookIssueAdmin)

