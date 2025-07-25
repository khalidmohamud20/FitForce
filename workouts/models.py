from django.db import models

# Create your models here.
class Workout(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)

class Exercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    reps = models.IntegerField()
    sets = models.IntegerField()

