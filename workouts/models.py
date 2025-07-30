from django.db import models
from django.contrib.auth.models import User

DIFFICULTY_LEVELS = [
    ('beginner', 'Beginner'),
    ('intermediate', 'Intermediate'),
    ('advanced', 'Advanced'),
]

class Workout(models.Model):
    # Final: user is now required (non-nullable)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    exercises = models.ManyToManyField('Exercise', through='WorkoutExercise')

    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_LEVELS, default='beginner')

    def __str__(self):
        return self.name

class WorkoutExercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    reps = models.IntegerField()
    sets = models.IntegerField()

    def __str__(self):
        return f"{self.exercise.name} in {self.workout.name} - {self.sets} sets x {self.reps} reps"
