from django.shortcuts import render
from uuid import UUID

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from .models import Task
from .forms import TaskForm
from .services import TaskService


def index(request):
    response = TaskService.get_all()
    return render(request, 'tasks/index.html', response)


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


def detail(request, task_id):
    response = TaskService.get_by_id(task_id=task_id)
    form: TaskForm = TaskForm(instance=response)

    if request.method == 'POST':
        form: TaskForm = TaskForm(request.POST, instance=response)
        if form.is_valid():
            form.save()
            response = TaskService.get_all()
            return render(request, 'tasks/index.html', response)

    return render(request, 'tasks/detail.html', {'form': form, 'task_id': task_id})


def delete(request, task_id):
    task: Task = TaskService.get_by_id(task_id=task_id)
    task.delete()

    response = TaskService.get_all()
    return render(request, 'tasks/index.html', response)


@api_view(['POST'])
def create_from_api(request: Request) -> Response:
    service = TaskService()
    data = service.create_from_view(data=request.data)
    return Response(data=data, status=HTTP_201_CREATED)
