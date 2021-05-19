from groceries.serializers import GroceryItemSerializer
from django.conf.urls import url

from groceries.views import (
    GroceryStoreListView,
    GroceryItemListView,
    IngredientListView,
    RecipeListView
)

urlpatterns = [
    url(r'^stores/$',
        GroceryStoreListView.as_view(),
        name='api.groceries.stores'
    ),
    url(r'^items/$',
        GroceryItemListView.as_view(),
        name='api.groceries.items'
    ),
    url(r'^ingredients/$',
        IngredientListView.as_view(),
        name='api.groceries.ingredients'
    ),
    url(r'^recipes/$',
        RecipeListView.as_view(),
        name='api.groceries.recipes'
    ),
]
