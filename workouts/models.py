from django.db import models
from django.contrib.auth.models import User

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="Untitled Workout")
    description = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")

    CATEGORY_CHOICES = [
        ('strength', 'Strength'),
        ('cardio', 'Cardio'),
        ('flexibility', 'Flexibility'),
        ('endurance', 'Endurance'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='strength')

    def __str__(self):
        return f"Workout: {self.name} by {self.user.username} on {self.date.strftime('%Y-%m-%d')}"
