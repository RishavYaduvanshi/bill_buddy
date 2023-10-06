from datetime import datetime
from uuid import uuid4
from ariadne import MutationType

mutation = MutationType()


@mutation.field("createTransaction")
def resolve_create_transaction(
    _, info, transaction_name, transaction_amount, split_by, split_group_id
):
    from transaction_management.models import Transaction
    from user_management.models import Person
    from group_management.models import Group


    group = Group.objects.get(pk=split_group_id)
    transaction = Transaction(
        transaction_id=str(uuid4()),
        transaction_name=transaction_name,
        transaction_amount=transaction_amount,
        split_by=Person.objects.get(pk=split_by),
        split_group_id=group,
        transaction_date=datetime.now(),
    )
    transaction.save()
    transaction.split_with.set(group.members.all(), clear=True)
    transaction.save() 

    transaction_obj = {
        "transaction_id": transaction.transaction_id,
        "transaction_name": transaction.transaction_name,
        "transaction_amount": transaction.transaction_amount,
        "split_by": transaction.split_by,
        "split_group_id": transaction.split_group_id,
        "transaction_date": transaction.transaction_date,
        "split_with": transaction.split_with.all(),
    }
    return transaction_obj