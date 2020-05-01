from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', records_list, name="list"),
    path('create/', record_create, name="create"),
    path('new/', record_new, name="new"),
    path('update/<int:pk>', record_update, name="update"),
    path('delete/<int:pk>', record_delete, name="delete"),
]


