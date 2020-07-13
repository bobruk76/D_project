from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'pets'
urlpatterns = [
    path('animal/create', AnimalCreate.as_view(), name='animal_create'),
    path('animal/', AnimalList.as_view(), name='animal_list'),
    path('animal/<int:pk>/', AnimalUpdate.as_view(), name='animal_edit'),
    path('animal/<int:pk>/delete/', AnimalDelete.as_view(), name='animal_delete'),

    path('', IndexPageView.as_view()),
    path('contacts/', ContactsView.as_view()),
]
