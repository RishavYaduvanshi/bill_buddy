from ariadne import  make_executable_schema, load_schema_from_path
from group_management.schema.query import query
from group_management.schema.mutation import mutation

query_defs = load_schema_from_path("group_management/schema/query/query.graphql")
mutation_defs = load_schema_from_path("group_management/schema/mutation/mutation.graphql")
stiched_defs = load_schema_from_path("group_management/schema/stiched-schema.graphql")

type_defs = query_defs + mutation_defs + stiched_defs

schema  = make_executable_schema(type_defs,query,mutation)