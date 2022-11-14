from django.db import models


class Tags(models.Model):
    name = models.CharField(max_length=127)


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True)
    is_completed = models.BooleanField()
    tags = models.ManyToManyField(Tags, related_name="tasks")
