from django.contrib import admin

from .models import Author, Paragraph, Comment

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    fields = ["username"]

admin.site.register(Author, AuthorAdmin)
admin.site.register(Paragraph)
admin.site.register(Comment)
