from django.urls import path
from .views import Home
from .views import *

urlpatterns = [
    path('', Records.as_view()),
    path('create/', RecordCreate.as_view()),
    path('record/<int:pk>/delete/', RecordDeleteView.as_view(), name='record_delete'),
    path('record/<int:pk>/update/', RecordUpdateView.as_view(), name='record_update'),
    # path('meal/update/', MealUpdateView.as_view(), name='meal_update'),
    path('mealingredient/create/<int:pk>', MealIngredientCreateView.as_view(), name='mealingredient_create'),
    path('spisok/', Spisok.as_view()),
    path('/meal/update', mealupdate)
]
