from django.db import models
from django.contrib import admin


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    unit = models.CharField(max_length=5)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeContainsIngredient')

    def __str__(self):
        return self.name

class Step(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    instruction = models.CharField(max_length=1000)
    duration = models.DurationField()

class RecipeContainsIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=7, decimal_places=2)
