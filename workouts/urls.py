from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'workouts'  # Namespace for workouts app

urlpatterns = [
    # Home page (root URL)
    path('', views.home_view, name='home'),
    path('home/', views.home_view, name='home_alt'),  # Optional additional home URL

    # Workout-related pages
    path('workouts/', views.workout_list, name='workout_list'),
    path('add/', views.workout_add, name='workout_add'),
    path('<int:pk>/edit/', views.workout_edit, name='workout_edit'),
    path('<int:pk>/delete/', views.workout_delete, name='workout_delete'),

    # Static pages
    path('about/', views.about_view, name='about'),

    # User authentication
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
