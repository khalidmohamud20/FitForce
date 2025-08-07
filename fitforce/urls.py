# fitforce/urls.py

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from workouts import views as workout_views


urlpatterns = [
    path('admin/', admin.site.urls),

    # Built-in Django auth views
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
path('home/', workout_views.home_view, name='home_direct'),

    # Workouts app
    path('workouts/', include('workouts.urls', namespace='workouts')),

    # Redirect root to workout list
    path('', lambda request: redirect('workouts:workout_list')),
]
