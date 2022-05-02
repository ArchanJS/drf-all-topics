from django.shortcuts import render
from rest_framework import viewsets
from .models import Note
from .serializers import NoteSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from .modthrottle import ModRateThrottle

# Create your views here.

class NoteViewSet(viewsets.ModelViewSet):
    queryset=Note.objects.all()
    serializer_class=NoteSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    throttle_classes=[AnonRateThrottle,ModRateThrottle]