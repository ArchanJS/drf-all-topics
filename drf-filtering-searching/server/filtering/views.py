from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Post
from .serializers import PostSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter


# Create your views here.

class PostList(ListAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

    # <--Filtering using default filter method-->
    
    # def get_queryset(self):
    #     return Post.objects.filter(title='title 1')

    # <--Filtering using django-filter package-->

    # filter_backends=[DjangoFilterBackend]
    # filterset_fields=['title','content']

    # <--Searching-->
    # '^' - Starts with
    # '=' - Exact match
    # '@' - Full text search
    # '$' - Regex search
    # search_fields=['title','content'] 
    # search_fields=['^title'] 

    filter_backends=[SearchFilter,OrderingFilter]
    ordering_fields=['title','content'] # ?ordering=title

# Skipped pagination, limit-offset pagination, cursor pagination