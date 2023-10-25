from uuid import uuid4
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from ariadne_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
import json
from user_management.schema import schema
from user_management.models import Person
from django.utils import timezone

# Create your views here.

graphql_view = GraphQLView.as_view(schema=schema)


@csrf_exempt
def login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        try:
            person = Person.objects.get(email=email)
        except:
            return JsonResponse({"message":"Invalid Credentials"})
        if person.check_password(password):
            return JsonResponse({"message":"Login Successful"})
        else:
            return JsonResponse({"message":"Invalid Credentials"})
    

    

