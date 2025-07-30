from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Workout, Exercise, WorkoutExercise
from .forms import CustomUserCreationForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def workouts(request):
    level = request.GET.get('level', 'all')
    all_exercises = Exercise.objects.all()

    if level in ['beginner', 'intermediate', 'advanced']:
        filtered = all_exercises.filter(difficulty=level)
    else:
        filtered = all_exercises

    if request.method == 'POST':
        if request.user.is_authenticated:
            workout = Workout.objects.create(user=request.user, name='Custom Workout')
            for exercise in filtered:
                if str(exercise.id) in request.POST.getlist('selected_exercises'):
                    reps = int(request.POST.get(f'reps_{exercise.id}', 0))
                    sets = int(request.POST.get(f'sets_{exercise.id}', 0))
                    WorkoutExercise.objects.create(
                        workout=workout,
                        exercise=exercise,
                        reps=reps,
                        sets=sets
                    )
            return redirect('home')
        else:
            return redirect('login')

    return render(request, 'workouts/workouts.html', {
        'exercises': filtered,
        'level': level,
    })

def exercise_detail(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    return render(request, 'workouts/exercise_detail.html', {'exercise': exercise})

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
