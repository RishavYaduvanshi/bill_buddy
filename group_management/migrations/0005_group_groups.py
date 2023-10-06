# Generated by Django 4.2.5 on 2023-09-26 08:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_management", "0010_remove_person_groups"),
        ("group_management", "0004_remove_group_id_alter_group_created_at_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="group",
            name="groups",
            field=models.ManyToManyField(
                related_name="group_members", to="user_management.person"
            ),
        ),
    ]