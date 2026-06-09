import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # 'admin' will be stored in DB, while 'Admin' will be showed to the users
    id = models.UUIDField(
        primary_key= True,
        default=uuid.uuid4,
        editable=False
    )
    
    ROLE_CHOICES = (('admin', 'Admin'), ('student', 'Student'), )
    role = models.CharField(max_length= 20, choices= ROLE_CHOICES, default='student' )
