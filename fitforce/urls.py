"""
URL configuration for fitforce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('workouts.urls')),  # App-level routes (home, signup, about, etc.)
    path('accounts/', include('django.contrib.auth.urls')),  # Optional: for built-in auth views like password reset
]
