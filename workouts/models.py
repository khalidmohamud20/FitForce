from django.db import models
from django.contrib.auth.models import User

class Exercise(models.Model):
    DIFFICULTY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='beginner')

    def __str__(self):
        return self.name

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)  # Removed name field
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Workout by {self.user.username} on {self.date}"

class WorkoutExercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='workout_exercises')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.PositiveIntegerField(default=3)
    reps = models.PositiveIntegerField(default=10)

    def __str__(self):
        return f"{self.exercise.name} in workout on {self.workout.date}"
