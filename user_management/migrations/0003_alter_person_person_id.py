# Generated by Django 4.2.5 on 2023-09-21 10:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_management", "0002_remove_person_id_person_person_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="person_id",
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]