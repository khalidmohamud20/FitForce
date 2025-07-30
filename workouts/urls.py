from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    path('workouts/', views.workouts, name='workouts'),
    path('my-workouts/', login_required(views.my_workouts), name='my_workouts'),

    path('exercise/<int:pk>/', views.exercise_detail, name='exercise_detail'),

    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('signup/', views.signup_view, name='signup'),
]
