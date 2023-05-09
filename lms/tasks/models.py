from django.db import models
from django.contrib.auth import get_user_model

from users.models import CustomUser


User = get_user_model()


class Task(models.Model):
    """Task model."""

    name = models.CharField(max_length=150, verbose_name='task name')

    class Meta:
        verbose_name = 'task'
        verbose_name_plural = 'tasks'

    def __str__(self):
        return self.name


class Teacher(models.Model):
    """Teacher model"""

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='teacher',
        )

    def __str__(self):
        return self.user.username


class StudentGroup(models.Model):
    """Group of students model."""

    name = models.CharField(max_length=50, verbose_name='name of group')
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        related_name='group',
        verbose_name='teacher',
        help_text='Teacher',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class Student(models.Model):
    """Student model"""

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='student'
        )
    group = models.ForeignKey(
        StudentGroup,
        on_delete=models.SET_NULL,
        related_name='student',
        verbose_name='group',
        help_text='Group',
        blank=True,
        null=True
    )
    tasks = models.ManyToManyField(Task, through="Mark")

    def __str__(self):
        return self.user.username


class Mark(models.Model):
    """Mark model"""

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='mark',
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='mark'
    )
    value = models.DecimalField(max_digits=5, decimal_places=2)
