import graphene
from graphene_django.types import DjangoObjectType

from ..models import Ingredient, Recipe, Step

class IngredientType(DjangoObjectType):
    quantity = graphene.Float()
    
    def resolve_quantity(instance, info):
        if hasattr(info.context, 'recipe_id'):
            recipe_id = info.context.recipe_id
            relation = instance.recipecontainsingredient_set.get(recipe=Recipe.objects.get(id=recipe_id))
            return relation.quantity

    class Meta:
        model = Ingredient

class RecipeType(DjangoObjectType):
    class Meta:
        model = Recipe
    
    def resolve_ingredients(instance, info):
        info.context.recipe_id = instance.id

class StepType(DjangoObjectType): 
    def resolve_duration(self, info):
        return self.duration.total_seconds()

    class Meta:
        model = Step