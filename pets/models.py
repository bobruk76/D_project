import uuid

from django.utils.translation import gettext_lazy as _
from django.core import validators
from django.db import models
from django.urls import reverse

# Create your models here.
class Aninal(models.Model):

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=256, verbose_name="Кличка")
    age = models.IntegerField(verbose_name="Возраст",
                              validators=[validators.MaxValueValidator(40)])
    photo = models.ImageField(upload_to='pets_photo', blank=True)
    breed = models.ForeignKey('pets.Breed', on_delete=models.CASCADE,
                              verbose_name="Порода")

    def __str__(self):
        return "{} ({}, {})".format(self.name, self.breed)

    def get_absolute_url(self):
        return reverse('animal-detail', kwargs={'pk': self.pk})