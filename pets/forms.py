from django import forms
from pets.models import *

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'

