from rest_framework import serializers
from .models import Recipe, Step, Ingredient, RecipeContainsIngredient


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name', 'unit', 'quantity']
        
class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ['instruction', 'duration']

class RecipeSerializer(serializers.ModelSerializer):
    # ingredients = IngredientSerializer(many=True, read_only=True)
    steps = StepSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ['name', 'ingredients', 'steps']
        depth = 1
