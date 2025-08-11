from django import forms
from .models import Workout

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'description', 'duration', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Workout Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Description'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Duration (minutes)'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
