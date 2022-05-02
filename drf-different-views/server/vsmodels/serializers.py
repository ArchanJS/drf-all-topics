from rest_framework import serializers
from .models import Item

# Serializers

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields='__all__'