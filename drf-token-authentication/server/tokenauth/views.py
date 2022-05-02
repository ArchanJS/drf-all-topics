from django.shortcuts import render
from rest_framework import viewsets
from .serializers import NoteSerializer
from .models import Note
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class NoteViewSets(viewsets.ModelViewSet):
    queryset=Note.objects.all()
    serializer_class=NoteSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]