from django.shortcuts import render
from rest_framework import viewsets
from .serializers import NoteSerializer
from .models import Note
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

# Create your views here.

class NoteViewSet(viewsets.ModelViewSet):
    queryset=Note.objects.all()
    serializer_class=NoteSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]