from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Workout
from .forms import WorkoutForm


# Home View - shows login form styled like workouts page
def home_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('workouts:workout_list')
    else:
        form = AuthenticationForm()

    return render(request, 'workouts/home.html', {'form': form})


# Sign Up View
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created successfully!")
            login(request, user)  # Auto login after sign-up
            return redirect('workouts:workout_list')
        else:
            messages.error(request, "There was an error. Please correct the form.")
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})


# Logout View
@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('workouts:home')
    return render(request, 'registration/logout_confirm.html')


# Workout List View
@login_required(login_url='login')
def workout_list(request):
    workouts = Workout.objects.filter(user=request.user).order_by('-date')
    return render(request, 'workouts/workouts.html', {'workouts': workouts})


# Add Workout View
@login_required(login_url='login')
def workout_add(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user

            if not workout.name:
                workout.name = "Default Workout Name"
            if not workout.description:
                workout.description = "No description provided."

            workout.save()
            messages.success(request, 'Workout added successfully.')
            return redirect('workouts:workout_list')
    else:
        form = WorkoutForm()

    return render(request, 'workouts/form.html', {
        'form': form,
        'form_title': 'Add Workout',
        'submit_text': 'Save Workout'
    })


# Edit Workout View
@login_required(login_url='login')
def workout_edit(request, pk):
    workout = get_object_or_404(Workout, pk=pk, user=request.user)
    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            workout = form.save(commit=False)

            if not workout.name:
                workout.name = "Default Workout Name"
            if not workout.description:
                workout.description = "No description provided."

            workout.save()
            messages.success(request, 'Workout updated successfully.')
            return redirect('workouts:workout_list')
    else:
        form = WorkoutForm(instance=workout)

    return render(request, 'workouts/form.html', {
        'form': form,
        'form_title': 'Edit Workout',
        'submit_text': 'Update Workout'
    })


# Delete Workout View
@login_required(login_url='login')
def workout_delete(request, pk):
    workout = get_object_or_404(Workout, pk=pk, user=request.user)
    if request.method == 'POST':
        workout.delete()
        messages.success(request, 'Workout deleted successfully.')
        return redirect('workouts:workout_list')
    return render(request, 'workouts/workout_confirm_delete.html', {'workout': workout})


# About Page View - requires login
@login_required(login_url='login')
def about_view(request):
    return render(request, 'workouts/about.html')


# Workouts Page View - requires login
@login_required(login_url='login')
def workouts_page(request):
    return render(request, 'workouts/workouts.html')
