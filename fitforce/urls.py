from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('workouts/', include('workouts.urls', namespace='workouts')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', lambda request: redirect('workouts:workout_list')),  # redirect root to workouts list
]
