from pyexpat import model
from rest_framework import serializers
from .models import Comment

# Serializers

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'