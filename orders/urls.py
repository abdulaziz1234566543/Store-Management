from django.contrib import admin
from django.urls import path
from . import views
from .views import *
urlpatterns = [


    path("list/", OrderListView.as_view(), name="Order-list"),
    path("create/", OrderCreateView.as_view(), name="Create-Order"),
    path("update/<int:pk>/", OrderUpdateView.as_view(), name="Update"),
    path("retrieve/<int:pk>/", OrderRetrieveView.as_view(), name="Retrieve"),
    path("delete/<int:pk>/", OrderDeleteView.as_view(), name="Delete"),
]
