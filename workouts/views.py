from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Workout, Exercise
from .forms import CustomUserCreationForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# ⛔ Removed @login_required to make workouts page public
def workouts(request):
    level = request.GET.get('level', 'all')
    all_exercises = Exercise.objects.all()

    if level in ['beginner', 'intermediate', 'advanced']:
        filtered = all_exercises.filter(difficulty=level)
    else:
        filtered = all_exercises

    if request.method == 'POST':
        if request.user.is_authenticated:
            selected_ids = request.POST.getlist('selected_exercises')
            workout = Workout.objects.create(user=request.user, name='Custom Workout')
            for eid in selected_ids:
                reps = request.POST.get(f'reps_{eid}')
                sets = request.POST.get(f'sets_{eid}')
                ex = get_object_or_404(Exercise, id=eid)
                workout.exercises.add(ex, through_defaults={'reps': reps, 'sets': sets})
            return redirect('home')
        else:
            return redirect('login')  # Optional: prevent POST from anonymous users

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
