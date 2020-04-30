# -*- coding: utf-8 -*-

from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('course_list_page/', views.course_list_page, name='course_list_page'),
    path('professor_list_page/', views.professor_list_page, name='professor_list_page'),
    path('student_list_page/', views.student_list_page, name='student_list_page'),
    path('course_page/', views.course_page, name='course_page'),
    path('professor_page/', views.professor_page, name='professor_page'),
    path('student_page/', views.student_page, name='student_page'),
    path('project_page/', views.project_page, name='project_page')
]