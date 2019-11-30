from django.contrib import admin

from .models import Recipe, Ingredient, Step, RecipeContainsIngredient

class RecipeContainsIngredientInline(admin.TabularInline):
    model = RecipeContainsIngredient
    extra = 2

class RecipeAdmin(admin.ModelAdmin):
    inlines = (RecipeContainsIngredientInline,)

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(Step)
