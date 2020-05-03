from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import *

def home_page(request):
    return student_page(request, 2)

def course_list_page(request):
    return HttpResponse("Hello, world. You're at the course list page.")
    pass

def professor_list_page(request):
    return HttpResponse("Hello, world. You're at the professor list page.")
    pass

def student_list_page(request):
    pass

def course_page(request, course_abbreviation):
    pass

def professor_page(request, professor_eid):
    p = Professor.objects.get(eid=professor_eid)
    latest_project_list = p.projects.all()
    context = {'object_list': latest_project_list}
    return render(request, 'projectapp/linked_list.html', context)

def student_page(request, student_eid):
    s = Student.objects.get(eid=student_eid)
    latest_project_list = s.projects.all()
    context = {'object_list': latest_project_list}
    return render(request, 'projectapp/linked_list.html', context)

def project_page(request, project_id):
    p = Project.objects.get(id=project_id)
    latest_project_list = Project.objects.order_by('title')
    context = {'object_list': latest_project_list}
    return render(request, 'projectapp/detailed_template.html', context)
