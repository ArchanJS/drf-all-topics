from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from .cpermissioins import PostPermission

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[PostPermission]