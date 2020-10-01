from typing import Optional, Dict, List

from django.db.models import Manager


class TaskManager(Manager):

    def load_all(self) -> List:
        return super().all()

    def get_by_id(self, id: int):
        from tasks.models import Task
        try:
            task: Task = Task.objects.filter(id=id).first()
        except Task.DoesNotExist:
            task: Optional[Task] = None

        return task

    def update(self, id: int, data: Dict):
        return super().filter(pk=id).update(**data)

    def delete(self, id: int):
        return super().filter(pk=id).delete()
