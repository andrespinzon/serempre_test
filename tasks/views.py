from django.shortcuts import render

from .models import Task


def index(request):
    tasks = Task.objects.load_all()
    context = {'tasks': tasks}
    return render(request, 'tasks/index.html', context)

