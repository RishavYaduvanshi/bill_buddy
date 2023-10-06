from ariadne import QueryType

query = QueryType()

@query.field("getAllGroups")
def resolve_get_name(_,info):
    from group_management.models import Group
    group_info = Group.objects.all()
    response = [
        {    
            "group_id": group.group_id,
            "group_name": group.group_name,
            "group_length": group.group_length,
            "created_by": group.created_by,
            "group_member": group.members.all(),
            "created_at": group.created_at,
            "updated_at": group.updated_at,
            
        } for group in group_info
    ]

    return response

@query.field("getGroup")
def resolve_get_group(_,info,group_id):
    from group_management.models import Group
    group_info = Group.objects.get(group_id=group_id)
    response = {    
        "group_id": group_info.group_id,
        "group_name": group_info.group_name,
        "group_length": group_info.group_length,
        "created_by": group_info.created_by,
        "group_member": group_info.members.all(),
        "created_at": group_info.created_at,
        "updated_at": group_info.updated_at,
        
    }
    return response

@query.field("getGroupTransaction")
def resolve_get_group_transaction(_,info,group_id):
    from group_management.models import Group
    from transaction_management.models import Transaction
    try:
        group_info = Group.objects.get(group_id=group_id)
    except:
        raise Exception("Group not found")
    
    trasaction_info = Transaction.objects.filter(split_group_id=group_info)
    response = []
    for transaction in trasaction_info:
        split_amount = transaction.transaction_amount/group_info.group_length 
        split_with = []
        for member in transaction.split_with.all():
            if member == transaction.split_by:
                split_with.append({
                    "member_id": member.person_id,
                    "member_name": member.name,
                    "amount": split_amount,
                    "status": True,
                })
            else:
                split_with.append({
                    "member_id": member.person_id,
                    "member_name": member.name,
                    "amount": split_amount,
                    "status": False,
                })
        response.append({
            "transaction_id": transaction.transaction_id,
            "transaction_name": transaction.transaction_name,
            "transaction_amount": transaction.transaction_amount,
            "split_by": transaction.split_by,
            "group_id": group_id,
            "transaction_date": transaction.transaction_date,
            "split_with": split_with,
        })
    return response

    