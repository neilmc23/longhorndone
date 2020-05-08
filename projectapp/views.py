from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import *

def login_page(request):
    # Refernce straight to the login page html
    return render(request, 'projectapp/login.html')

def home_page(request):
    # Reference straight to the home page html
    return render(request, 'projectapp/home.html')

def course_list_page(request):
    # Gathers latest courses
    latest_course_list = Course.objects.all()
    # Passes page name and course list to html
    context = {'object_name': 'UT Austin Course List', 'object_list': latest_course_list}
    return render(request, 'projectapp/linked_list.html', context)

def professor_list_page(request):
    # Gathers latest professors
    latest_professor_list = Professor.objects.all()
    # Passes page name and professor list to html
    context = {'object_name': 'UT Austin Professor List', 'object_list': latest_professor_list}
    return render(request, 'projectapp/linked_list.html', context)

def student_list_page(request):
    # Gathers latest students
    latest_student_list = Student.objects.all()
    # Passes page name and student list to html
    context = {'object_name': 'UT Austin Student List', 'object_list': latest_student_list}
    return render(request, 'projectapp/linked_list.html', context)

def course_page(request, course_link):
    # Finds course with given course link
    c = [ ci for ci in Course.objects.all() if ci.get_link() == course_link ][0]
    # Gathers latest projects
    latest_project_list = c.project_set.all()
    # Passes course name/semester and project list to html
    context = {'object_name': str(c), 'project_info': latest_project_list}
    return render(request, 'projectapp/tiled.html', context)

def professor_page(request, professor_eid):
    # Finds professor with given eid
    p = Professor.objects.get(eid=professor_eid)
    # Gathers latest courses
    latest_course_list = p.courses.all()
    # Passes professor name and course list to html
    context = {'object_name': p.name, 'object_list': latest_course_list}
    return render(request, 'projectapp/linked_list.html', context)

def student_page(request, student_eid):
    # Finds student with given eid
    s = Student.objects.get(eid=student_eid)
    # Gathers latest projects
    latest_project_list = s.project_set.all()
    # Passes professor name and project list to html
    context = {'object_name': s.name, 'project_info': latest_project_list}
    return render(request, 'projectapp/tiled.html', context)

def project_page(request, project_id):
    # Finds project with given id
    p = Project.objects.get(id=project_id)
    # Passes project into html
    context = {'item': p}
    return render(request, 'projectapp/detailed.html', context)
