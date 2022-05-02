from dataclasses import fields
from rest_framework import serializers
from .models import Post

# Serialiers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'