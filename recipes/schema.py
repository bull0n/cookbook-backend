import graphene



class Query(recipes.schema.Query, graphene.ObjectType):
    pass

class Mutation(recipes.schema.Mutation, graphene.ObjectType):
    pass