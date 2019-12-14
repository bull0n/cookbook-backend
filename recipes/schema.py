import graphene

from .graphql_definitions.query import Query
from .graphql_definitions.mutations import UpdateRecipe


class Query(Query, graphene.ObjectType):
    pass

class Mutation(graphene.ObjectType):
    update_recipe = UpdateRecipe.Field()
