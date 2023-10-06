from ariadne import make_executable_schema, load_schema_from_path

from transaction_management.schema.query import query
from transaction_management.schema.mutation import mutation

query_defs = load_schema_from_path("transaction_management/schema/query/query.graphql")
mutation_defs = load_schema_from_path("transaction_management/schema/mutation/mutation.graphql")
stiched_type_defs = load_schema_from_path("transaction_management/schema/stiched-schema.graphql")

type_defs = query_defs+mutation_defs+stiched_type_defs


schema = make_executable_schema(type_defs,query,mutation)