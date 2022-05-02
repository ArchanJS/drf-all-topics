from django.shortcuts import render
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer

# Create your views here.

class ItemViewwset(viewsets.ModelViewSet):
    queryset=Item.objects.all()
    serializer_class=ItemSerializer

# Here user only can read data. So only get request will work here
# class ItemViewwset(viewsets.ReadOnlyModelViewSet):
#     queryset=Item.objects.all()
#     serializer_class=ItemSerializer