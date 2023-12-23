from django.db import models
from django.contrib.auth.models import User
# Create your models here.

PRIORITIES = [
    ('LOW', 'Low'),
    ('MEDIUM', 'Medium'),  
    ('HIGH', 'High'),
]


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    # TODO: add photos field later
    priority = models.CharField(max_length=10, choices=PRIORITIES, default='LOW') 
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('priority', 'due_date')

    def __str__(self):
        return self.title
