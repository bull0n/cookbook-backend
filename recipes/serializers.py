from rest_framework import serializers
from .models import Recipe, Step, Ingredient, RecipeContainsIngredient

class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = ['name', 'ingredients']

class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = ['name', 'unit', 'quantity']
