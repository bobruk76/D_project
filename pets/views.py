from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render

from django.http.response import HttpResponseRedirect
from django.views.generic import ListView, DetailView, TemplateView
from django.forms import formset_factory
from pets.forms import AnimalForm
from pets.models import (Animal)
from django.urls import reverse_lazy

# Create your views here.
class IndexPageView(TemplateView):
    template_name = 'index.html'

class ContactsView(TemplateView):
    template_name = 'contacts.html'


class AnimalList(ListView):
    model = Animal
    template_name = 'animals.html'


class AnimalDetailView(DetailView):
    model = Animal
    template_name = '_view.html'

