from rest_framework import serializers
from .models import User,UserRole,Product,OrderItem,Order

class registerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['email','password']

class userSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    role = serializers.CharField(required=False)
    class Meta:
        model = User
        fields = '__all__'

class productSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class orderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'

class orderItemSerializer(serializers.ModelSerializer):
    price = Product.objects.values_list('price')
    # product = Product.product_name
    class Meta:
        model = OrderItem
        fields = '__all__'

