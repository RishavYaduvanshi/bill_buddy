from django.contrib import admin
# Register your models here.

from .models import Group
@admin.register(Group)
class GroupRegistered(admin.ModelAdmin):
    list_display = ("group_id","group_name")
    filter_horizontal = ("members",)