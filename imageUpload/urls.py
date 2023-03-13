from django.contrib import admin
from . import views
from django.urls import path, include

# app_name = 'imageUpload'

urlpatterns = [
    path('', views.home, name='home'),
    path('imageprocess', views.imageprocess, name='imageprocess'),
]
