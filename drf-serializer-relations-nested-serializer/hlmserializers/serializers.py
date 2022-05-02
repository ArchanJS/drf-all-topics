from rest_framework import serializers
from .models import Note

# Serializers

class NoteSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:note-detail")
    class Meta:
        model=Note
        fields=('id','url','title','content')