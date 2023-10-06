from django.db import models
from uuid import uuid4

# Create your models here.

class Person(models.Model):
    person_id = models.CharField(primary_key=True,max_length=100,editable=False,default=uuid4)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    age = models.IntegerField()
    created_at = models.DateField()
    updated_at = models.DateField()

    
    