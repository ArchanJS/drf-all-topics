from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView
from .models import Post
from .serializers import PostSerializer
from rest_framework.throttling import ScopedRateThrottle

# Create your views here.

class PostList(ListAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='viewpost'

class PostRetreieve(RetrieveAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='viewpost'

class PostCreate(CreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='modifypost'

class PostUpdate(UpdateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='modifypost'

class PostDestroy(DestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='modifypost'