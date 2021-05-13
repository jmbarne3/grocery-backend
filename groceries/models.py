from django.db import models
from multiselectfield import MultiSelectField
from fractions import Fraction

# Create your models here.
class GroceryStore(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class Measurement(models.Model):
    abbr = models.CharField(max_length=10, null=False, blank=False)
    name = models.CharField(max_length=25, null=False, blank=False)

    def __unicode__(self):
        return f"{self.name} ({self.abbr})"

    def __str__(self):
        return f"{self.name} ({self.abbr})"


class GroceryItem(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    extra_info = models.CharField(max_length=255, null=True, blank=True)
    preferred_store = models.ForeignKey(GroceryStore, on_delete=models.CASCADE)

    def __unicode__(self):
        return f"{self.name} - {self.preferred_store}"

    def __str__(self):
        return f"{self.name} - {self.preferred_store}"


class Ingredient(models.Model):
    amount = models.FloatField(null=False, blank=False)
    measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE)
    item = models.ForeignKey(GroceryItem, on_delete=models.CASCADE, related_name='ingredients')

    @property
    def simple_amount(self):
        ALLOWED_DENOMINATORS = [2, 3, 4, 8]

        frac = Fraction(self.amount)
        if frac.denominator in ALLOWED_DENOMINATORS:
            return str(frac)
        else:
            return str(self.amount)

    def __unicode__(self):
        return f"{self.simple_amount} {self.measurement.abbr} {self.item.name}"

    def __str__(self):
        return f"{self.simple_amount} {self.measurement.abbr} {self.item.name}"


class Recipe(models.Model):
    MEAL_CHOICES = (
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('dessert', 'Dessert'),
        ('snack', 'Snack')
    )

    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    meal = MultiSelectField(null=False, blank=False, choices=MEAL_CHOICES)
    ingredients = models.ManyToManyField(Ingredient, related_name='recipes')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

