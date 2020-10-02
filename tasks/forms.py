from django.forms import ModelForm, CharField, IntegerField, FloatField, BooleanField, Textarea

from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            'developer', 'title', 'description', 'time_worked',
            'estimated_time', 'is_completed',
        ]
