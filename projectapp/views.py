from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import *

def home_page(request):
    return HttpResponse("Hello, world. You're at the home page.")
    pass

def course_list_page(request):
    return HttpResponse("Hello, world. You're at the course list page.")
    pass

def professor_list_page(request):
    return HttpResponse("Hello, world. You're at the professor list page.")
    pass

def student_list_page(request):
    pass

def course_page(request):
    pass

def professor_page(request):
    pass

def student_page(request):
    pass

def project_page(request):
    pass
