from django.shortcuts import render
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

# Create your views here.

class CommentList(GenericAPIView,ListModelMixin):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class CommentCreate(GenericAPIView,CreateModelMixin):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class CommentRetrieve(GenericAPIView,RetrieveModelMixin):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

class CommentUpdate(GenericAPIView,UpdateModelMixin):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

class CommentDestroy(GenericAPIView,DestroyModelMixin):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)