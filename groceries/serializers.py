from rest_framework import serializers

from groceries.models import (
    GroceryStore,
    GroceryItem,
    Ingredient,
    Recipe
)

class GroceryStoreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = GroceryStore

class GroceryItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = GroceryItem

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'simple_repr', 'amount', 'measurement']
        model = Ingredient

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)

    class Meta:
        fields = '__all__'
        model = Recipe
