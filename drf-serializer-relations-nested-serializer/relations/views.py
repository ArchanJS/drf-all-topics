from django.shortcuts import render
from .models import Person,Post
from .serializers import PersonSerializer,PostSerializer
from rest_framework import viewsets

# Create your views here.

class PersonViewset(viewsets.ModelViewSet):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer

class PostViewset(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer