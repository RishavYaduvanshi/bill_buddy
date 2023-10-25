from django.contrib import admin
from .models import Person
# Register your models here.

@admin.register(Person)
class PersonRegistered(admin.ModelAdmin):
    list_display = [('username')]
 