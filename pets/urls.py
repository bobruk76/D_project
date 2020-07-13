from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'pets'
urlpatterns = [
    path('animal/', AnimalList.as_view(), name='animal_list'),
    path('animal/<uuid:pk>/', AnimalDetailView.as_view(), name='animal_view'),


    path('', IndexPageView.as_view()),
    path('contacts/', ContactsView.as_view()),
]
