# Generated by Django 4.2.5 on 2023-09-28 09:00

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("group_management", "0011_alter_group_created_by"),
    ]

    operations = [
        migrations.CreateModel(
            name="Trasaction",
            fields=[
                (
                    "transaction_id",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("transaction_name", models.CharField(default=None, max_length=200)),
                ("transaction_amount", models.FloatField()),
                ("created_by", models.CharField(max_length=200)),
                ("created_at", models.DateField()),
                (
                    "group",
                    models.ManyToManyField(
                        related_name="transactions", to="group_management.group"
                    ),
                ),
            ],
        ),
    ]
