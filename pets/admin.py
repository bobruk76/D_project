from django.contrib import admin
from .models import (Animal, Breed)

# [admin.site.register(item) for item in (Book, Author, Reader, BookReading)]

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    pass

@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    pass