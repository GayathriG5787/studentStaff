import uuid

from django.db import models
from django.conf import settings

class Student(models.Model):
    id = models.UUIDField(
        primary_key= True,
        default=uuid.uuid4,
        editable=False
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    roll_number = models.CharField(
        max_length=20,
        unique=True
    )
    DEPARTMENT_CHOICES = (
        ('CSE', 'Computer Science and Engineering'),
        ('IT', 'Information Technology'),
        ('ECE', 'Electronics and Communication Engineering'),
        ('EEE', 'Electrical and Electronics Engineering'),
    )
    department = models.CharField(
        max_length=10,
        choices=DEPARTMENT_CHOICES
    )
    year = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return self.user.username
