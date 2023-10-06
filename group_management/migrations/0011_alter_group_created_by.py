# Generated by Django 4.2.5 on 2023-09-28 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("user_management", "0011_person_updared_at"),
        ("group_management", "0010_alter_group_members"),
    ]

    operations = [
        migrations.AlterField(
            model_name="group",
            name="created_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="created_groups",
                to="user_management.person",
            ),
        ),
    ]
