from rest_framework import serializers
from .models import Recipe, Step, Ingredient, RecipeContainsIngredient


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'unit']
        
class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ['instruction', 'duration']

class RecipeContainsIngredientSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField(source='ingredient.id')
    name = serializers.ReadOnlyField(source='ingredient.name')
    unit = serializers.ReadOnlyField(source='ingredient.unit')

    class Meta:
        model = RecipeContainsIngredient
        fields = ['id', 'quantity', 'name', 'unit']

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = RecipeContainsIngredientSerializer(source='recipecontainsingredient_set', many=True, read_only=True)
    steps = StepSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'ingredients', 'steps']