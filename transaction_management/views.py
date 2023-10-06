import json
from django.shortcuts import render
from ariadne_django.views import GraphQLView
from transaction_management.schema import schema
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
graphql_view = GraphQLView.as_view(schema=schema)

@csrf_exempt
def createTransaction(request):
    from .models import Transaction
    from uuid import uuid4
    from user_management.models import Person
    from group_management.models import Group
    from datetime import datetime
    from django.http import HttpResponse

    data = request.body.decode("utf-8")
    data = json.loads(data)
    transaction_name = data.get("transaction_name")
    transaction_amount = data.get("transaction_amount")
    split_by = data.get("split_by")
    split_group_id = data.get("split_group_id")
    group = Group.objects.get(pk=split_group_id)


    transaction = Transaction(
        transaction_id=str(uuid4()),
        transaction_name=transaction_name,
        transaction_amount=transaction_amount,
        split_by=Person.objects.get(pk=split_by),
        split_group_id=group,
        transaction_date=datetime.now(),
    )
    transaction.save()
    transaction.split_with.set(group.members.all(), clear=True)
    transaction.save() 

    
                
    return HttpResponse(str(transaction.__dict__))