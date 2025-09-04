from django.contrib import admin
from django.urls import path
from . import views
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [

    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("list/", UserListView.as_view(), name="User-list"),
    path("create/", UserCreateView.as_view(), name="Create-user"),
    path("update/<int:pk>/", UserUpdateView.as_view(), name="Update"),
    path("retrieve/<int:pk>/", UserRetrieveView.as_view(), name="Retrieve"),
    path("delete/<int:pk>/", UserDeleteView.as_view(), name="Delete"),
]

