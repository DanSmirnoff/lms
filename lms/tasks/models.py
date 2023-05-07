from django.db import models


class Task(models.Model):
    """Task model."""

    title = models.CharField(max_length=150, verbose_name='task title')

    class Meta:
        verbose_name = 'task'
        verbose_name_plural = 'tasks'

    def __str__(self):
        return self.title
