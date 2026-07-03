from django.db import models

# Create your models here
"""
there is models.Charfield(maxlength=length)
          '.TextField()
          '.DateTimeField(auto_now_add=True) 
          '.IntegerField(default=0)
          '.EmailField()
          '.BooleanField()
          '.

"""
class Department(models.Model):
          name=models.CharField(max_length=30)
          head_of_dept=models.CharField(max_length=60)
          budget=models.IntegerField()
          
          def __str__(self):
                    return self.name
          
class Course(models.Model):
          name=models.CharField(max_length=60)
          code=models.CharField(max_length=10)
          credits=models.IntegerField(default=0)
          department=models.ForeignKey(Department,on_delete=models.CASCADE)
          
          def __str__(self):
                    return self.name
          
class Student(models.Model):
          first_name=models.CharField(max_length=20)
          last_name=models.CharField(max_length=20)
          email=models.EmailField(unique=True);
          department=models.ForeignKey(Department,on_delete=models.CASCADE)
          enrollment_year=models.IntegerField()
          
          def __str__(self):
                    return f"{self.first_name} {self.last_name}"


class Enrollment(models.Model):
          student=models.ForeignKey(Student,on_delete=models.CASCADE)
          course=models.ForeignKey(Course,on_delete=models.CASCADE)
          enrollment_date=models.DateField()
          grade=models.CharField(max_length=1,blank=True)
          
          class Meta:
                    unique_together=[['student','course']]
          
          def __str__(self):
                    return f"{self.student} - {self.course}"
          

          
