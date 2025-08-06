from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Workout
from .forms import WorkoutForm

# Home view
def home_view(request):
    return render(request, 'workouts/home.html')

# Workout List View — shows workouts for all users (no login required)
def workout_list(request):
    workouts = Workout.objects.all().order_by('-date')  # Show all workouts (no filter for user)
    return render(request, 'workouts/workouts.html', {'workouts': workouts})

# Add Workout View — no login required
def workout_add(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save()  # No need for user authentication
            messages.success(request, 'Workout added successfully.')
            return redirect('workouts:workout_list')
    else:
        form = WorkoutForm()
    return render(request, 'workouts/workout_form.html', {'form': form})

# Edit Workout View — no login required (does not check for the user)
def workout_edit(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    
    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            messages.success(request, 'Workout updated successfully.')
            return redirect('workouts:workout_list')
    else:
        form = WorkoutForm(instance=workout)
    return render(request, 'workouts/workout_form.html', {'form': form})

# Delete Workout View — no login required (does not check for the user)
def workout_delete(request, pk):
    workout = get_object_or_404(Workout, pk=pk)

    if request.method == 'POST':
        workout.delete()
        messages.success(request, 'Workout deleted successfully.')
        return redirect('workouts:workout_list')
    return render(request, 'workouts/workout_confirm_delete.html', {'workout': workout})

# About Page View
def about_view(request):
    return render(request, 'workouts/about.html')

# Create Workout View — same as workout_add
def workout_create(request):
    return workout_add(request)
