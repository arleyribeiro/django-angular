from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from shopping.models import ShoppingItem
from shopping.serializers import ShoppingItemSerializer

class ShoppingItemViewSet(viewsets.ModelViewSet):
	
	serializer_class = ShoppingItemSerializer
	queryset = ShoppingItem.objects.all()
	#print(queryset)
