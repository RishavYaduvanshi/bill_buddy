
from datetime import datetime
from uuid import uuid4
from django.contrib.auth.hashers import make_password
from ariadne import MutationType
mutation = MutationType()

@mutation.field("addUser")
def resolve_add_user(_,info,username,password,first_name,last_name,email,age):
    from user_management.models import Person
    person = Person(
        person_id = str(uuid4()),
        username=username,
        password=make_password(password),
        first_name=first_name,
        last_name=last_name,
        email=email,
        age=age,
    )
    person.save()
    return person

@mutation.field("loginUser")
def resolve_login_user(_,info,email,password):
    from user_management.models import Person
    person = Person.objects.get(email=email)
    if person.check_password(password):
        return person
    else:
        return None

