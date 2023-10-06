from uuid import uuid4
from django.db import models
from user_management.models import Person
from group_management.models import Group

# Create your models here.

class Transaction(models.Model):
    transaction_id = models.CharField(primary_key=True,max_length=100,editable=False,default=uuid4)
    transaction_name = models.CharField(max_length=200, default=None)
    transaction_amount = models.FloatField()
    split_by = models.ForeignKey("user_management.Person", on_delete=models.RESTRICT, related_name='split_by_transactions')
    split_group_id = models.ForeignKey("group_management.Group", on_delete=models.RESTRICT, related_name='group_transactions')
    transaction_date = models.DateField()
    split_with = models.ManyToManyField('user_management.Person', related_name='split_transactions')

    
