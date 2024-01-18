# Taskapproval_app/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Department(models.Model):
    name = models.CharField(max_length=50)

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(default=timezone.now)


class TaskCompletion(models.Model):
    original_task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='original_task')
    new_task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='new_task')
