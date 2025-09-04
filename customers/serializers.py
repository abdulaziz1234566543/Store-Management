from rest_framework import serializers
from .models import User
from products.serializers import ProductSerializer

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ["id", "name", "email","password"]
        extra_kwargs = {
            "password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password")  # remove password from dict
        user = User(**validated_data)
        user.set_password(password)  # hash the password
        user.save()
        return user
