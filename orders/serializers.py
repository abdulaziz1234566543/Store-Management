from rest_framework import serializers
from .models import Order
from customers.models import User
from products.models import Product


class OrderSerializer(serializers.ModelSerializer):
    # Only show names in the response
    product_name = serializers.CharField(source="product.name", read_only=True)
    user_name = serializers.CharField(source="user.name", read_only=True)

    # Accept names when creating, but don't show in response
    product = serializers.SlugRelatedField(
        queryset=Product.objects.filter(stock__gt=0),
        slug_field="name",
        write_only=True
    )


    class Meta:
        model = Order
        fields = ["id", "user_name", "product_name", "product",  "quantity", "created_at"]
        extra_kwargs = {
            "user": {"write_only": True},
            "product": {"write_only": True},
        }

    def validate_quantity(self, value):

        if value <= 0:
            raise serializers.ValidationError("Quantity must be greater than 0")
        return value

    def validate(self, data):

        product = data['product']
        quantity = data['quantity']

        if product.stock < quantity:
            raise serializers.ValidationError({
                'quantity': f'Insufficient stock. Only {product.stock} units available.'
            })
        return data