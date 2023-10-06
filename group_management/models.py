from uuid import uuid4
from django.db import models
from user_management.models import Person

# Create your models here.

class Group(models.Model):
    group_id = models.CharField(primary_key=True,max_length=100,editable=False,default=uuid4)
    group_name = models.CharField(max_length=200)
    group_length = models.IntegerField(default=1 )
    created_by = models.ForeignKey("user_management.Person", on_delete=models.RESTRICT, related_name='created_groups')
    created_at = models.DateField()
    updated_at = models.DateField()

    members = models.ManyToManyField('user_management.Person', related_name='groups')
