```
from rest_framework import serializers
from .models import Department,Course,Student,Enrollment

class DepartmentSerializer(serializers.ModelSerializer):
          class Meta:
                    model=Department
                    fields='__all__'

class CourseSerializer(serializers.ModelSerializer):
          class Meta:
                    model=Course
                    fields='__all__'
class StudentSerializer(serializers.ModelSerializer):
          class Meta:
                    model=Student
                    fields='__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
          class Meta:
                    model=Enrollment
                    fields='__all__'
```

![alt text](image.png)
![alt text](image-1.png)
![alt text](image-2.png)
![alt text](image-3.png)
![alt text](image-4.png)
![alt text](image-5.png)
![alt text](image-6.png)