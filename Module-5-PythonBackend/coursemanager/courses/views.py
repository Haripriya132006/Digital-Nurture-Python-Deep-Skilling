from django.shortcuts import render ,HttpResponse

# Create your views here.
def hello_view(request):
          return HttpResponse("Course Management API is running")