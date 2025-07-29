from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # Public workouts page — REMOVE login requirement in views.py if needed
    path('workouts/', views.workouts, name='workouts'),

    # Optional detail view for individual exercises
    path('exercise/<int:pk>/', views.exercise_detail, name='exercise_detail'),

    # Auth views
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('signup/', views.signup_view, name='signup'),
]
