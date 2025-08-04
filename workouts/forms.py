from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Workout

class SignUpForm(UserCreationForm):  # Renamed from CustomUserCreationForm
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email address'
        })
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})
            self.fields[fieldname].help_text = None
        self.fields['email'].help_text = None

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['description']
