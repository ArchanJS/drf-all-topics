from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer
import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import JsonResponse

# Create your views here.

# Create post
@api_view(['POST'])
def create_post(request):
    try:
        io_data=io.BytesIO(request.body)
        parsed_data=JSONParser().parse(io_data)
        serialized_data=PostSerializer(data=parsed_data)
        if serialized_data.is_valid():
            serialized_data.save()
            return JsonResponse({'message':'Post created!'},status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return JsonResponse({'error':'Somehting went wrong!'},status=status.HTTP_400_BAD_REQUEST)

#Get all posts
@api_view(['GET'])
def get_all_posts(request):
    try:
        raw_posts=Post.objects.all()
        serialized_all_posts=PostSerializer(raw_posts,many=True)
        return JsonResponse(serialized_all_posts.data,safe=False,status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return JsonResponse({'error':'Somehting went wrong!'},status=status.HTTP_400_BAD_REQUEST)

# Get post by id
@api_view(['GET'])
def get_a_post(request,id):
    try:
        raw_post=Post.objects.get(id=id)
        serialized_post=PostSerializer(raw_post)
        return JsonResponse(serialized_post.data,status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return JsonResponse({'error':'Something went wrong!'},status=status.HTTP_400_BAD_REQUEST)

# Update a post completely
@api_view(['PUT'])
def update_a_post_put(request,id):
    try:
        raw_body_data=request.body
        io_body_data=io.BytesIO(raw_body_data)
        parsed_body_data=JSONParser().parse(io_body_data)
        raw_post=Post.objects.get(id=id)
        serialized_post=PostSerializer(raw_post,data=parsed_body_data,partial=True)
        if serialized_post.is_valid():
            serialized_post.save()
            return JsonResponse({'message':'Post completely updated!'},status=status.HTTP_200_OK)
        else:
            return JsonResponse({'error':'Something went wrong!'},status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)
        return JsonResponse({'error':'Something went wrong!'},status=status.HTTP_400_BAD_REQUEST)

# Update a post partially
@api_view(['PATCH'])
def update_a_post_patch(request,id):
    try:
        raw_body_data=request.body
        io_body_data=io.BytesIO(raw_body_data)
        parsed_body_data=JSONParser().parse(io_body_data)
        raw_post=Post.objects.get(id=id)
        serialized_post=PostSerializer(raw_post,data=parsed_body_data,partial=True)
        if serialized_post.is_valid():
            serialized_post.save()
            return JsonResponse({'message':'Post partially updated!'},status=status.HTTP_200_OK)
        else:
            return JsonResponse({'error':'Something went wrong!'},status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)
        return JsonResponse({'error':'Something went wrong!'},status=status.HTTP_400_BAD_REQUEST)

# Delete a post
@api_view(['DELETE'])
def delete_a_post(request,id):
    try:
        post=Post.objects.get(id=id)
        post.delete()
        return JsonResponse({'message':'Post deleted!'},status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return JsonResponse({'error':'Something went wrong!'},status=status.HTTP_400_BAD_REQUEST)