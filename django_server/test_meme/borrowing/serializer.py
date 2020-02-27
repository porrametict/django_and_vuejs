from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Borrowing, Product


# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff']


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class BorrowingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Borrowing
        fields = '__all__'

