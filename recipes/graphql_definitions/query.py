
import graphene
from graphene_django.types import ObjectType

from ..models import Recipe, Ingredient, Step
from .types import RecipeType, IngredientType, StepType

class Query(object):
    recipe = graphene.Field(RecipeType, id=graphene.Int())
    recipes = graphene.List(RecipeType)
    steps = graphene.List(StepType)
    ingredients = graphene.List(IngredientType)

    def resolve_recipe(self, info, recipe_id):
        return Recipe.objects.get(id=recipe_id)

    def resolve_recipes(self, info, **kwargs):
        return Recipe.objects.all()
    