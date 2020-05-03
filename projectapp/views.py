from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import *

def home_page(request):
    pass

def course_list_page(request):
    latest_course_list = Course.objects.all()
    context = {'object_name': 'UT Austin Course List', 'object_list': latest_course_list}
    return render(request, 'projectapp/linked_list.html', context)

def professor_list_page(request):
    latest_professor_list = Professor.objects.all()
    context = {'object_name': 'UT Austin Professor List', 'object_list': latest_professor_list}
    return render(request, 'projectapp/linked_list.html', context)

def student_list_page(request):
    latest_student_list = Student.objects.all()
    context = {'object_name': 'UT Austin Student List', 'object_list': latest_student_list}
    return render(request, 'projectapp/linked_list.html', context)

def course_page(request, course_abbreviation):
    c = Course.objects.get(abbreviation=course_abbreviation)
    latest_project_list = c.projects.all()
    context = {'object_name': c.name, 'object_list': latest_project_list}
    return render(request, 'projectapp/linked_list.html', context)

def professor_page(request, professor_eid):
    p = Professor.objects.get(eid=professor_eid)
    latest_project_list = p.projects.all()
    context = {'object_name': p.name, 'object_list': latest_project_list}
    return render(request, 'projectapp/linked_list.html', context)

def student_page(request, student_eid):
    s = Student.objects.get(eid=student_eid)
    latest_project_list = s.projects.all()
    context = {'object_name': s.name, 'object_list': latest_project_list}
    return render(request, 'projectapp/linked_list.html', context)

def project_page(request, project_id):
    p = Project.objects.get(id=project_id)
    latest_project_list = Project.objects.order_by('title')
    context = {'object_list': latest_project_list}
    return render(request, 'projectapp/detailed_template.html', context)
