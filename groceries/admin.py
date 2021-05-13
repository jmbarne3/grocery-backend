from groceries.models import GroceryStore
from django.contrib import admin

from .models import *

# Register your models here.
@admin.register(GroceryStore)
class GroceryStoreAdmin(admin.ModelAdmin):
    pass

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    pass

@admin.register(GroceryItem)
class GroceryItemAdmin(admin.ModelAdmin):
    pass

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass
