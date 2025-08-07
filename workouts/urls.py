from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'workouts'

urlpatterns = [
    # Home page (now the default page when you click FitForce)
    path('', views.home_view, name='home'),

    # Workout List page
    path('workouts/', views.workout_list, name='workout_list'),

    # Add Workout page
    path('add/', views.workout_add, name='workout_add'),

    # Edit Workout page
    path('<int:pk>/edit/', views.workout_edit, name='workout_edit'),

    # Delete Workout page
    path('<int:pk>/delete/', views.workout_delete, name='workout_delete'),

    # About page
    path('about/', views.about_view, name='about'),

    # Sign-up page
    path('signup/', views.signup_view, name='signup'),

    # Login page (must use the one with "Sign up here")
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    # Logout
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
