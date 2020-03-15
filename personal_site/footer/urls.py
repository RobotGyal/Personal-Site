from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from footer import views as footer_views

urlpatterns = [
    path('', footer_views.contact, name = 'contact'), 
    path('success/', footer_views.success, name = 'success')
]