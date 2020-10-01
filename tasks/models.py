from datetime import datetime

from django.db.models import AutoField, CharField, BooleanField, DateTimeField, Model, PositiveIntegerField, FloatField

from tasks.managers import TaskManager


class Task(Model):
    id: int = AutoField(primary_key=True)
    developer: str = CharField('Developer', max_length=255, null=False)
    title: str = CharField('Title', max_length=255, null=False)
    description: str = CharField('Description', max_length=32, null=False)
    time_worked: int = PositiveIntegerField('Time Worked')
    estimated_time: float = FloatField('Estimated Time')
    is_completed: bool = BooleanField('Is Completed', default=True, null=False)
    created_at: datetime = DateTimeField('Created', auto_now_add=True, db_index=True)
    updated_at: datetime = DateTimeField('Updated', auto_now=True)

    objects: TaskManager = TaskManager()
