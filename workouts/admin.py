from django.contrib import admin

# Register your models here.
# workouts/admin.py
from django.contrib import admin
from .models import Workout, Exercise

admin.site.register(Workout)
admin.site.register(Exercise)
