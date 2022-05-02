from dataclasses import fields
from rest_framework import serializers
from .models import Student

# Serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'