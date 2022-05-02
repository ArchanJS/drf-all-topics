from rest_framework import serializers
from .models import Person,Post

# Serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=['id','title','content','postedby']


class PersonSerializer(serializers.ModelSerializer):
    # person=serializers.StringRelatedField(many=True,read_only=True)  Here data includes the titles of the posts created by the users
    # person=serializers.PrimaryKeyRelatedField(many=True,read_only=True)  Here data includes the ids of the posts created by the users
    # person=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='api:post-detail')   Here data includes the links of the posts created by the users **(api->app_name and namespace in urls.py and person->basename in urls.py)
    # person=serializers.SlugRelatedField(many=True,read_only=True,slug_field='title')   Here data includes the titles of the posts created by the users **(api->app_name and namespace in urls.py and person->basename in urls.py)
    # person=serializers.HyperlinkedIdentityField(view_name='api:person-detail')   Here data includes the links of the first post created by the users **(api->app_name and namespace in urls.py and person->basename in urls.py)
    postdet=PostSerializer(many=True,read_only=True,source='person') # Generating post details along with posts (like populate in mongodb)
    class Meta:
        model=Person
        # fields=['id','name','email','person'] -> for serializer.field
        fields=['id','name','email','postdet']
        #fields=('id','name','email','person') -> Here the data includes the ids of the posts created by the users 