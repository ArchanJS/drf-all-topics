from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Post

# Serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'