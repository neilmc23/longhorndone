from django.db import models
import random


class Project(models.Model):
    title = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=50, default='')
#    course = models.CharField(max_length=50, default='')
#    students = models.ForeignKey(Student, default = '1', on_delete=models.CASCADE)
#    tags = models.CharField(max_length=50, default='')
    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=50, default='')
    abbreviation = models.CharField(max_length=50, default='')
    semester = models.CharField(max_length=50, default='')
    #professors = models.ManyToManyField
    projects = models.ManyToManyField(Project)
    def __str__(self):
        return self.abbreviation + ' ' + self.semester


class Student(models.Model):
    name = models.CharField(max_length=50, default='')
    eid = models.CharField(max_length=50, default='')
    projects = models.ManyToManyField(Project)
    def __str__(self):
        return self.name


class Professor(models.Model):
    name = models.CharField(max_length=50, default='')
    eid = models.CharField(max_length=50, default='')
    courses = models.ManyToManyField(Course)
    def __str__(self):
        return self.name


class Tag(models.Model):
    title = models.CharField(max_length=50, default='')
    projects = models.ManyToManyField(Project)
    def __str__(self):
        return self.title
