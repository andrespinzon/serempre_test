from django.shortcuts import render

from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.load_all()
    context = {'tasks': tasks}
    return render(request, 'tasks/index.html', context)


def create(request):
    if request.method == 'POST':
        form: TaskForm = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            tasks = Task.objects.load_all()
            context = {'tasks': tasks}
            return render(request, 'tasks/index.html', context)
    else:
        form: TaskForm = TaskForm()

    return render(request, 'tasks/create.html', {'form': form})


