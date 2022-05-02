from functools import partial
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from .serializers import StudentSerializer
from .models import Student
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
import io
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@api_view(['GET','POST','PUT','PATCH','DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def studentAPIs(request,pk=None):
    try:
        id=pk
        if request.method == 'POST':
            io_data=io.BytesIO(request.body)
            json_data=JSONParser().parse(io_data)
            serializer=StudentSerializer(data=json_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'message':'Student created!'},status=status.HTTP_201_CREATED)
            return JsonResponse({'error':'Something went wrong!'},status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'GET':
            students=Student.objects.all()
            serializer=StudentSerializer(students,many=True)
            return JsonResponse(serializer.data,safe=False,status=status.HTTP_200_OK)
        elif id is not None:
            student=Student.objects.get(id=id)
            if request.method == 'PUT':
                io_data=io.BytesIO(request.body)
                json_Data=JSONParser().parse(io_data)
                serializer=StudentSerializer(student,data=json_Data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse({'message':'Student completely updated!'},status=status.HTTP_200_OK)
                else:
                    return JsonResponse({'error':'Something went wrong!'},status=status.HTTP_400_BAD_REQUEST)
            elif request.method == 'PATCH':
                io_data=io.BytesIO(request.body)
                json_Data=JSONParser().parse(io_data)
                serializer=StudentSerializer(student,data=json_Data,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse({'message':'Student partially updated!'},status=status.HTTP_200_OK)
                else:
                    return JsonResponse({'error':'Something went wrong!'},status=status.HTTP_400_BAD_REQUEST)
            else:
                student.delete()
                return JsonResponse({'message':'Student deleted!'},status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return JsonResponse({'error':'Something went wrong!'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)