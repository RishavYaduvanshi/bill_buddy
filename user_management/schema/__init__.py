from ariadne import make_executable_schema, load_schema_from_path
from user_management.schema.query import query
from user_management.schema.mutation import mutation,login_response



query_type_defs = load_schema_from_path("user_management/schema/query/query.graphql")
mutation_type_defs = load_schema_from_path("user_management/schema/mutation/mutation.graphql")
stiched_type_defs = load_schema_from_path("user_management/schema/stiched-schema.graphql")

type_defs = query_type_defs + mutation_type_defs + stiched_type_defs


# Create the executable schema
schema = make_executable_schema(type_defs,[query,mutation,login_response])