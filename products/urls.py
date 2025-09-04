from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path("list/", ProductList.as_view(), name="product-list"),
    path("create/", ProductCreate.as_view(), name="product-create"),
    path("retrieve/<int:pk>/", ProductRetrieve.as_view(), name="product-retrieve"),
    path("update/<int:pk>/", ProductUpdate.as_view(), name="product-update"),
    path("delete/<int:pk>/", ProductDelete.as_view(), name="product-delete"),
]