from functools import partial
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TeacherSerializer
from .models import Teacher
from django.http import JsonResponse
from rest_framework import status
import io
from rest_framework.parsers import JSONParser

# Create your views here.

class TeacherViewsets(viewsets.ViewSet):
    def list(self,request):
        teachers=Teacher.objects.all()
        serializers=TeacherSerializer(teachers,many=True)
        return JsonResponse(serializers.data,safe=False,status=status.HTTP_200_OK)

    def retrieve(self,request,pk=None):
        if pk is not None:
            teacher=Teacher.objects.get(id=pk)
            serializer=TeacherSerializer(teacher)
            return JsonResponse(serializer.data,safe=False,status=status.HTTP_200_OK)
        return JsonResponse({'error':'Something went wrong!'},status=status.HTTP_400_BAD_REQUEST)

    def create(self,request):
            try:
                io_data=io.BytesIO(request.body)
                json_data=JSONParser().parse(io_data)
                serializer=TeacherSerializer(data=json_data)
                print(serializer)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse({'message':'Teacher created!'},status=status.HTTP_201_CREATED)
                return JsonResponse({'error':'Something went wrong!'},status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                print(e)
                return JsonResponse({'error':'Something went wrong!'},status=status.HTTP_400_BAD_REQUEST)
    def update(self,request,pk=None):
        if pk is not None:
            teacher=Teacher.objects.get(id=pk)
            io_data=io.BytesIO(request.body)
            json_data=JSONParser().parse(io_data)
            serializer=TeacherSerializer(teacher,data=json_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'message':'Fully updated!'},status=status.HTTP_200_OK)
            return JsonResponse({'error':'Something went wrong!'},status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,request,pk=None):
        if pk is not None:
            teacher=Teacher.objects.get(id=pk)
            io_data=io.BytesIO(request.body)
            json_data=JSONParser().parse(io_data)
            serializer=TeacherSerializer(teacher,data=json_data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'message':'Partially updated!'},status=status.HTTP_200_OK)
            return JsonResponse({'error':'Something went wrong!'},status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk=None):
        if pk is not None:
            teacher=Teacher.objects.get(id=pk)
            teacher.delete()
            return JsonResponse({'message':'Teacher deleted!'},status=status.HTTP_200_OK)
        return JsonResponse({'error':'Something went wrong!'},status=status.HTTP_400_BAD_REQUEST)