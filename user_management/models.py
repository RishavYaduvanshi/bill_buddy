from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from uuid import uuid4
# Create your models here.

class Person(AbstractUser):
    person_id = models.CharField(primary_key=True, max_length=100, editable=False, default=uuid4)
    first_name = models.CharField(max_length=30,default="first_name")
    last_name = models.CharField(max_length=30,default="last_name")
    email = models.EmailField()
    age = models.IntegerField(default=23)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    
    