from django.db import models

from accounts.models import MyUser

class TodoList(models.Model):
    tasks = models.CharField(max_length=100)
    owner = models.ForeignKey('accounts.MyUser', related_name='todo_lists', on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    completed_task = models.BooleanField(default=False)
    not_completed_task = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.tasks
    
    def total_tasks(self):
        return self.completed_tasks.count() + self.incompleted_tasks.count()
    
    def completed_percentage(self):
        total_tasks = self.total_tasks()
        if total_tasks == 0:
            return 0
        return (self.completed_tasks.count() / total_tasks) * 100
    
    def remaining_tasks(self):
        return self.incompleted_tasks.count()

