from django.db import models
import random


class Project(models.Model):
    name = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=50, default='')
    view_page = 'project_page_id'
    def get_link(self):
        return self.id
    def __str__(self):
        return self.title


class Course(models.Model):
    name = models.CharField(max_length=50, default='')
    abbreviation = models.CharField(max_length=50, default='')
    semester = models.CharField(max_length=50, default='')
    projects = models.ManyToManyField(Project)
    view_page = 'course_page_abbreviation'
    def get_link(self):
        return self.abbreviation
    def __str__(self):
        return self.abbreviation + ' ' + self.semester


class Student(models.Model):
    name = models.CharField(max_length=50, default='')
    eid = models.CharField(max_length=50, default='')
    projects = models.ManyToManyField(Project)
    view_page = 'student_page_eid'
    def get_link(self):
        return self.eid
    def __str__(self):
        return self.name


class Professor(models.Model):
    name = models.CharField(max_length=50, default='')
    eid = models.CharField(max_length=50, default='')
    courses = models.ManyToManyField(Course)
    view_page = 'professor_page_eid'
    def get_link(self):
        return self.eid
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, default='')
    projects = models.ManyToManyField(Project)
    def __str__(self):
        return self.title
