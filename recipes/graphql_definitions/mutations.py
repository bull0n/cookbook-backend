import graphene

from .types import RecipeType
from ..models import Recipe

class UpdateRecipe(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)

    ok = graphene.Boolean()
    recipe = graphene.Field(RecipeType)


    def mutate(self, info, name, id):
        question = Recipe.objects.get(pk=id)
        question.name = name
        question.save()
        # Notice we return an instance of this mutation
        return UpdateRecipe(question=question)