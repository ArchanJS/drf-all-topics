from dataclasses import fields
from rest_framework import serializers
from.models import Note

# Serializer

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Note
        fields='__all__'