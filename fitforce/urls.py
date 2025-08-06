from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin
    path('workouts/', include('workouts.urls', namespace='workouts')),  # Workouts app (with app_name defined)
    path('accounts/', include('django.contrib.auth.urls')),  # Django built-in auth URLs (login, logout, etc.)
    path('', lambda request: redirect('workouts:workout_list')),  # Redirect root to workout list
]
