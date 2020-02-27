from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.response import Response

from .serializer import ProductSerializers, UserSerializer, BorrowingSerializers
from .models import Product, Borrowing
from rest_framework import viewsets


# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    
class BorrowingViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializers

    def list(self, request):
        b = Borrowing.objects.all()
        b_data = BorrowingSerializers(b, many=True).data
        for i in range(len(b_data)):
            user_data = UserSerializer(b[i].user).data
            b_data[i]['user'] = user_data
            product_data = ProductSerializers(b[i].product).data
            b_data[i]['product'] = product_data

        return Response(b_data)
