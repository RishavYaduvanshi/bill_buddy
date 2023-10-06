
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("user_management.urls")),
    path("group/", include("group_management.urls")),
    path("transaction/", include("transaction_management.urls")),
]
