from django.urls import path
from . import views

app_name = 'workouts'

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('', views.workout_list, name='workout_list'),
    path('add/', views.workout_add, name='workout_add'),  # Update to workout_add instead of workout_create
    path('<int:pk>/edit/', views.workout_edit, name='workout_edit'),
    path('<int:pk>/delete/', views.workout_delete, name='workout_delete'),
    path('about/', views.about_view, name='about'),
]
