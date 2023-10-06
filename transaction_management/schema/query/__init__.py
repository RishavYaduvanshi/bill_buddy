from ariadne import QueryType

query = QueryType()

@query.field("getTransaction")
def resolve_get_transaction(_, info, transaction_id):
    from transaction_management.models import Transaction
    transaction = Transaction.objects.get(pk=transaction_id)
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
