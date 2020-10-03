from rest_framework.serializers import ModelSerializer
from .models import Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'developer', 'title', 'description', 'time_worked',
                  'estimated_time', 'is_completed')
