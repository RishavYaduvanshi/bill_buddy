from django.http import HttpResponse
from ariadne_django.views import GraphQLView
from group_management.schema import schema

# Create your views here.
graphql_view = GraphQLView.as_view(schema=schema)
