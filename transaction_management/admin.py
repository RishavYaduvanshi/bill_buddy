from django.contrib import admin

from transaction_management.models import Transaction

# Register your models here.


@admin.register(Transaction)
class TransactionRegistered(admin.ModelAdmin):
    list_display = ("transaction_id","transaction_name")