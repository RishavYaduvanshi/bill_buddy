from django.urls import path,include
from. import views
urlpatterns = [
    path('', views.graphql_view, name='graphql'),
    path('login', views.login, name='login'),
]