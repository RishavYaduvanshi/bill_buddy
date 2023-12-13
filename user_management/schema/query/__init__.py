from ariadne import QueryType
from auth import jwt_required

query = QueryType()


@query.field("getAllUsers")
@jwt_required
def resolve_get_all_users(_,info):
    from user_management.models import Person
    persons = Person.objects.all()
    response = [
        {
            'person_id': person.person_id,
            'username': person.username,
            'first_name': person.first_name,
            'last_name': person.last_name,
            'email': person.email,
            'age': person.age,
            'group_join': person.group_members.all(),
            'created_at': person.created_at,
            'updated_at': person.updated_at,
        }
        for person in persons
    ]
    return response

@query.field("getUser")
@jwt_required
def resolve_get_user(_,info,person_id):
    from user_management.models import Person
    person = Person.objects.get(person_id=person_id) 
    print(person.group_members.all().values_list('group_id', flat=True))
    response = {
        'person_id': person.person_id,
        'username': person.username,
        'first_name': person.first_name,
        'last_name': person.last_name,
        'email': person.email,
        'age': person.age,
        'group_join': person.group_members.all().values_list('group_id', flat=True),
        'created_at': person.created_at,
        'updated_at': person.updated_at,
    }
    return response