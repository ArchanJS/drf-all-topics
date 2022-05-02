from django.shortcuts import render
from rest_framework import viewsets
from .models import Note
from .serializers import NoteSerializer
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny

# Create your views here.

class NoteViews(viewsets.ModelViewSet):
    queryset=Note.objects.all()
    serializer_class=NoteSerializer

    # <--If we uncomment line 16th and 17th, global permissions won't work-->

    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]

    # Permission classes:
    #  AllowAny: Anyone can access
    # IsAuthenticated: Only authenticated users can access
    # IsAdminUser: Only admins and staffs can access