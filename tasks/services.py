from typing import Dict, Optional
from .models import Task
from common.soap_service import SoapService


class TaskService:

    @staticmethod
    def get_all() -> Dict:
        tasks = Task.objects.load_all()

        if len(tasks) > 1:
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
