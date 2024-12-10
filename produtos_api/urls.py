from django.contrib import admin
from django.urls import path, include
from .views import ProdutoListCreate

urlpatterns = [
    path('produtos/', ProdutoListCreate.as_view(), name='produto-list-create'),
]