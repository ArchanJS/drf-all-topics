from functools import partial
from django.http import JsonResponse
from django.shortcuts import render
from .serializers import NoteSerializer
from .models import Note
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
import io

# Create your views here.
 
class NoteAPIs(APIView):
    # Create note
    def post(self,request,format=None):
        try:
            io_data=io.BytesIO(request.body)
            json_data=JSONParser().parse(io_data)
            serialized_data=NoteSerializer(data=json_data)
            if serialized_data.is_valid():
                serialized_data.save()
                return JsonResponse({'message':'Note created!'},status=status.HTTP_201_CREATED)
            else:
                return JsonResponse({'error':'Somehting went wrong!'},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return JsonResponse({'error':'Somehting went wrong!'},status=status.HTTP_400_BAD_REQUEST)
    
    # Get a note
    def get(self,request,id,format=None):
        try:
            raw_data=Note.objects.get(id=id)
            serialized_data=NoteSerializer(raw_data)
            print(serialized_data)
            return JsonResponse(serialized_data.data,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return JsonResponse({'error':'Somehting went wrong!'},status=status.HTTP_400_BAD_REQUEST)
    
    # Update a note completely
    def put(self,request,id,format=None):
        try:
            note=Note.objects.get(id=id)
            io_data=io.BytesIO(request.body)
            parsed_data=JSONParser().parse(io_data)
            serialized_note=NoteSerializer(note,data=parsed_data,partial=True)
            if serialized_note.is_valid():
                serialized_note.save()
                return JsonResponse({'message':'Note completely updated!'},status=status.HTTP_200_OK)
            else:
                return JsonResponse({'error':'Somehting went wrong!'},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return JsonResponse({'error':'Somehting went wrong!'},status=status.HTTP_400_BAD_REQUEST)
    
    # Update a note partially
    def patch(self,request,id,format=None):
        try:
            note=Note.objects.get(id=id)
            io_data=io.BytesIO(request.body)
            parsed_data=JSONParser().parse(io_data)
            serialized_note=NoteSerializer(note,data=parsed_data,partial=True)
            if serialized_note.is_valid():
                serialized_note.save()
                return JsonResponse({'message':'Note partially updated!'},status=status.HTTP_200_OK)
            else:
                return JsonResponse({'error':'Somehting went wrong!'},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return JsonResponse({'error':'Somehting went wrong!'},status=status.HTTP_400_BAD_REQUEST)
    
    # Delete a note
    def delete(self,request,id,format=None):
        try:
            note=Note.objects.get(id=id)
            note.delete()
            return JsonResponse({'message':'Note deleted!'},status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return JsonResponse({'error':'Something went wrong!'},status=status.HTTP_400_BAD_REQUEST)