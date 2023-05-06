from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Custom user model."""

    STAFF = 'STF'
    TEACHER = 'TCH'
    STUDENT = 'STD'
    STATUS_CHOICES = (
        (STAFF, 'Staff'),
        (TEACHER, 'Teacher'),
        (STUDENT, 'Student'),
    )

    status = models.CharField(max_length=3,
                              choices=STATUS_CHOICES)

    def __str__(self):
        return self.username
