from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from ..core.models import User, GlucoseUnit, Insulin
from ..ingredients.models import Ingredient, IngredientUnit

class Record(models.Model):
    time = models.DateTimeField(auto_now=True)
    type = models.IntegerField(default=0)
    glucose_level = models.IntegerField(null = True, default = 0)
    glucose_level_unit = models.ForeignKey(GlucoseUnit, on_delete = models.SET_NULL, null = True)
    insulin_amount = models.FloatField(null = True, default = 0)
    insulin = models.ForeignKey(Insulin, on_delete = models.SET_NULL, null = True)
    bread_units = models.FloatField(null = True, default = 0)
    notes = models.CharField(max_length = 256, null = True)

class Meal(models.Model):
    record = models.ForeignKey(Record, on_delete = models.CASCADE, null = True)
    ingredient = models.ForeignKey(Ingredient, on_delete = models.CASCADE)
    ingredient_unit = models.ForeignKey(IngredientUnit, on_delete = models.CASCADE)
    quantity = models.FloatField(default=0)