
from datetime import datetime,timedelta
from uuid import uuid4
from django.contrib.auth.hashers import make_password
from ariadne import MutationType, UnionType
from user_management.models import Person

login_response = UnionType("LoginResponse")
mutation = MutationType()


def genrate_token(person):
    import jwt 
    secret_key = 'THIS IS A TEST SECRET KEY AND IS USED FOR TESTING!'
    payload = {
        'id': person.person_id,
        'exp': datetime.utcnow() + timedelta(hours=1),
        'iat': datetime.utcnow()
    }
    token = jwt.encode(payload, secret_key, algorithm='HS256').decode('utf-8')
    return token


@login_response.type_resolver
def resolve_login_response(obj, *_):
    if isinstance(obj, dict) and "token" in obj and "person" in obj:
        return "LoginPerson"
    if isinstance(obj, dict) and "message" in obj:
        return "Error"
    return None



@mutation.field("addUser")
def resolve_add_user(_,info,username,password,first_name,last_name,email,age):
    
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
def resolve_login_user(_, info, email, password):
    try:
        person = Person.objects.get(email=email)
        if person.check_password(password):
            genrate_token(person)
            response = {
                'token': genrate_token(person),
                'person': person
            } 
            return response
        else:
            return {'message': 'Password is incorrect'}
            
    except Person.DoesNotExist:
        return {'message': 'Email does not exist'}


