from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class StudentViewSets(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer