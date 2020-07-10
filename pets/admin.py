from django.contrib import admin
from .models import (Book, Author, Reader, BookReading, Publisher, BookPublishing)

# [admin.site.register(item) for item in (Book, Author, Reader, BookReading)]

@admin.register(Aninal)
class AuthorAdmin(admin.ModelAdmin):
    pass