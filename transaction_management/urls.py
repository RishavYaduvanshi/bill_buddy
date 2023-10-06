from django.urls import path,include
from. import views
urlpatterns = [
    path('', views.graphql_view, name='graphql'),
    path('test', views.createTransaction, name='ct'),
]