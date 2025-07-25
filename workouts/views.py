from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Workout
from .forms import CustomUserCreationForm  # Import your custom form

def home(request):
    workouts = Workout.objects.all()
    return render(request, 'home.html', {'workouts': workouts})

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in immediately after signup
            return redirect('home')  # Redirect to homepage after signup
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def about(request):
    print("About page accessed")  # optional debug print
    return render(request, 'about.html')
