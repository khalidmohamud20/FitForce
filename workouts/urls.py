from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'workouts'

urlpatterns = [
    path('', views.home_view, name='home'),  # Home page
    path('workouts/', views.workout_list, name='workout_list'),  # Workout list page
    path('workouts/add/', views.workout_add, name='workout_add'),  # Add workout page
    path('workouts/edit/<int:pk>/', views.workout_edit, name='workout_edit'),  # Edit workout page
    path('workouts/delete/<int:pk>/', views.workout_delete, name='workout_delete'),  # Delete workout page
    path('about/', views.about_view, name='about'),  # About page
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Login page
    # signup removed
]
