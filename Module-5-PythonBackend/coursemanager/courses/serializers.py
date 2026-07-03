from rest_framework import serializers
from .models import Department,Course,Student,Enrollment

class DepatmentSerializer(serializers.Model.Serializer):
          class Meta:
                    model=Department
                    fields='__all__'

class CourseSerializer(serializers.ModelSerializer):
          class Meta:
                    model=Course
                    fields='__all__'

# class StudentSerializer(serializers.ModelSerializer):
          # class Meta