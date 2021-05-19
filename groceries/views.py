from django.shortcuts import render
from rest_framework import generics

from groceries.models import (
    GroceryItem,
    GroceryStore,
    Ingredient,
    Recipe
)

from groceries.serializers import (
    GroceryItemSerializer,
    GroceryStoreSerializer,
    IngredientSerializer,
    RecipeSerializer
)

# Create your views here.
class GroceryStoreListView(generics.ListAPIView):
    queryset = GroceryStore.objects.all()
    serializer_class = GroceryStoreSerializer

class GroceryItemListView(generics.ListAPIView):
    queryset = GroceryItem.objects.all()
    serializer_class = GroceryItemSerializer

class IngredientListView(generics.ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class RecipeListView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
