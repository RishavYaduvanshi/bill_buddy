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

    

