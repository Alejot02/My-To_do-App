from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=1000, null=True)
    deadline = models.DateTimeField()

    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['deadline', 'title', 'created_at']