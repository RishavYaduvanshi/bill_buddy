
from datetime import datetime
from uuid import uuid4
from django.utils import timezone
from ariadne import MutationType
mutation = MutationType()

@mutation.field("addUser")
def resolve_add_user(_,info,name,email,age):
    from user_management.models import Person
    person = Person(
        person_id = str(uuid4()),
        name=name,
        email=email,
        age=age,
        created_at= datetime.now().date(),
        updated_at= datetime.now().date()

    )
    person.save()
    return person

