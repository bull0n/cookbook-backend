
from graphene_django.types import DjangoObjectType

from ..models import Ingredient, Recipe, Step

class RecipeType(DjangoObjectType):
    class Meta:
        model = Recipe

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient

class StepType(DjangoObjectType): 
    class Meta:
        model = Step