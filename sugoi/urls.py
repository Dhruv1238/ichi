from django import urls
from django.contrib import admin
from django.urls import path 
from sugoi import views

urlpatterns = [
    path("", views.index),
    path("home", views.home ),
    path("contact", views.contact ),
    path('form', views.form),
    path('submitted', views.submitted),
    path('history', views.history)


]