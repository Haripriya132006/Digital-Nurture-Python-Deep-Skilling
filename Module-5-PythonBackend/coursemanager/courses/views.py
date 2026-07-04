from django.shortcuts import render ,HttpResponse
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action

from .models import Course,Student,Enrollment
from .serializers import CourseSerializer,StudentSerializer,EnrollmentSerializer

# Create your views here.
def hello_view(request):
          return HttpResponse("Course Management API is running")

class CourseViewSet(viewsets.ModelViewSet):
          queryset = Course.objects.all()
          serializer_class = CourseSerializer
          
          # 34. Custom action: GET /api/courses/{id}/students/
          @action(detail=True, methods=['get'])
          def students(self, request, pk=None):
                    course = self.get_object() 
                    students = Student.objects.filter(enrollment__course=course) 
                    serializer = StudentSerializer(students, many=True)
                    return Response(serializer.data)
class StudentViewSet(viewsets.ModelViewSet):
          queryset=Student.objects.all()
          serializer_class=StudentSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
          queryset=Enrollment.objects.all()
          serializer_class=EnrollmentSerializer