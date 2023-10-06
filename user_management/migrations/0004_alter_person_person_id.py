# Generated by Django 4.2.5 on 2023-09-21 10:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("user_management", "0003_alter_person_person_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="person_id",
            field=models.CharField(
                default=uuid.uuid4,
                editable=False,
                max_length=100,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]