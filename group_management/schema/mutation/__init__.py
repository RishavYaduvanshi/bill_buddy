from uuid import uuid4
from ariadne import MutationType
from django.utils import timezone
from user_management import models as user_models

mutation = MutationType()

@mutation.field("createGroup")
def resolve_create_group(_,info,group_name,group_length,created_by):
    from group_management.models import Group
    
    group = Group(
        group_id = str(uuid4()),
        group_name=group_name,
        group_length=group_length,
        created_by=user_models.Person.objects.get(pk=created_by),
        created_at= timezone.now(),
        updated_at= timezone.now()
        )
    group.save()
    group.members.add(created_by)
    return group

@mutation.field("joinToGroup")
def resolve_join_to_group(_,info,person_id,group_id):
    from group_management.models import Group
    from user_management.models import Person
    group = Group.objects.get(group_id=group_id)
    person = Person.objects.get(person_id=person_id)
    if group.members.filter(person_id=person_id).exists():      
        raise Exception("Already joined")
    if group.group_length == group.members.all().count():
        raise Exception("Group is full")
    group.members.add(person)
    return group