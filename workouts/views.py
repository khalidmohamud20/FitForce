from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Workout
from .forms import WorkoutForm

def home_view(request):
    return render(request, 'workouts/home.html')

def workout_list(request):
    workouts = Workout.objects.all().order_by('-date')  # Show all workouts for now
    return render(request, 'workouts/workouts.html', {'workouts': workouts})

def workout_add(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = None  # Temporarily remove user assignment
            workout.save()
            messages.success(request, 'Workout added.')
            return redirect('workouts:workout_list')
    else:
        form = WorkoutForm()
    return render(request, 'workouts/workout_form.html', {'form': form})

def workout_edit(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            messages.success(request, 'Workout updated.')
            return redirect('workouts:workout_list')
    else:
        form = WorkoutForm(instance=workout)
    return render(request, 'workouts/workout_form.html', {'form': form})

def workout_delete(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    if request.method == 'POST':
        workout.delete()
        messages.success(request, 'Workout deleted.')
        return redirect('workouts:workout_list')
    return render(request, 'workouts/workout_confirm_delete.html', {'workout': workout})

def about_view(request):
    return render(request, 'workouts/about.html')
