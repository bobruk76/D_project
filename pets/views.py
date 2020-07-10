from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render

from django.http.response import HttpResponseRedirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.forms import formset_factory
from pets.forms import (AnimalForm,)
from pets.models import (Animal, Breed)
from django.urls import reverse_lazy

# Create your views here.
class AnimalList(ListView):
    model = Animal
    template_name = 'animal_list.html'

class AnimalCreate(CreateView):
    model = Animal
    form_class = AnimalForm
    template_name = '_edit.html'

class AnimalUpdate(UpdateView):
    model = Animal
    form_class = AnimalForm
    template_name = '_edit.html'

class AnimalDelete(DeleteView):
    model = Animal
    template_name = '_delete.html'