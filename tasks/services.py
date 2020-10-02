from typing import Dict, Optional
from .models import Task


class TaskService:

    @staticmethod
    def get_all() -> Dict:
        tasks = Task.objects.load_all()
        return {'tasks': tasks}

    @staticmethod
    def get_by_id(task_id: int) -> Optional[Task]:
        task: Task = Task.objects.get_by_id(id=task_id)
        return task
