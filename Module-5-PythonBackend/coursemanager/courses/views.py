from django.shortcuts import render ,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Course
from .serializers import CourseSerializer

# Create your views here.
def hello_view(request):
          return HttpResponse("Course Management API is running")

class CourseListView(APIView):
          def get(self,request):
                    courses=Course.objects.all()
                    serializer=CourseSerializer(courses,many=True)
                    return Response(serializer.data)

          def post(self,request):
                    serializer=CourseSerializer(data=request.data)
                    if serializer.is_valid():
                              serializer.save()
                              return Response(serializer.data,status=status.HTTP_201_CREATED)
                    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CourseDetailView(APIView):
          def get(self,request,pk):
                    course=get_object_or_404(Course,pk=pk)
                    serializer=CourseSerializer(course)
                    return Response(serializer.data)
          
          def put(self,request,pk):
                    course=get_object_or_404(Course,pk=pk)
                    serializer=CourseSerializer(course,data=request.data)
                    if serializer.is_valid():
                              serializer.save()
                              return Response(serializer.data)
                    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
          
          def delete(self,request,pk):
                    course=get_object_or_404(Course,pk=pk)
                    course.delete()
                    return Response(status=status.HTTP_204_NO_CONTENT)
          