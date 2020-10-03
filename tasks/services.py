from typing import Dict, Optional, Set
from .models import Task
from .serializers import TaskSerializer
from common.soap_service import SoapService

from rest_framework.exceptions import APIException
from django.core.exceptions import ValidationError
from django.db.transaction import atomic as atomic_transaction


class TaskService:

    data: Dict = None

    def __validate_allowed_fields(self, allowed_fields: Set, model_name: str):
        if not self.data or not isinstance(self.data, dict):
            raise APIException(detail='Invalid data.')
        for key in self.data:
            if key not in allowed_fields:
                raise APIException(detail=f'Invalid field "{key}" for {model_name} model.')

    def __validate_required_fields(self, required_fields: Set):
        for key in required_fields:
            if key not in self.data:
                raise APIException(detail=f'Key {key} is required.')

    @staticmethod
    def get_all() -> Dict:
        tasks = Task.objects.load_all()

        if len(tasks) >= 1:
            service = SoapService()
            for task in tasks:
                task.time_remaining = service.get_time_remaining(
                    task.time_worked,
                    task.estimated_time
                )
        return {'tasks': tasks}

    @staticmethod
    def get_by_id(task_id: int) -> Optional[Task]:
        task: Task = Task.objects.get_by_id(id=task_id)
        return task

    def create_from_view(self, data: Dict) -> Dict:
        self.data = data
        fields = {'developer', 'title', 'description', 'time_worked',
                  'estimated_time', 'is_completed'}
        self.__validate_allowed_fields(allowed_fields=fields, model_name='Task')
        self.__validate_required_fields(required_fields=fields)

        try:
            with atomic_transaction():
                task: Task = Task.objects.create(**data)
        except ValidationError as error:
            raise APIException(detail=error.messages[0])

        return TaskSerializer(instance=task).data
