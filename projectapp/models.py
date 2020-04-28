from django.db import models
import random

# Create your models here.

class Project(models.Model):
    def __init__(self, title, course, students, tags):
        self.project_id = self.generate_id
        self.title = title
        self.course = course
        self.students = students
        self.tags = tags
    def __str__(self):
        return self.title
    def generate_id(self):
        project_id = 'p'
        for i in range(10):
            project_id += random.randint(0, 9)
        return project_id
    

class Student(models.Model):
    def __init__(self, name):
        self.student_id = self.generate_id
        self.name = name
        self.projects = []
    def __str__(self):
        return self.name
    def generate_id(self):
        student_id = 's'
        for i in range(10):
            student_id += random.randint(0, 9)
        return student_id


class Professor(models.Model):
    def __init__(self, name):
        self.professor_id = self.generate_id
        self.name = name
        self.courses = []
    def __str__(self):
        return self.name
    def generate_id(self):
        professor_id = 's'
        for i in range(10):
            professor_id += random.randint(0, 9)
        return professor_id



class Course(models.Model):
    def __init__(self, title):
        self.title = title
    def __str__(self):
        return self.title
    

class Tag(models.Model):
    def __init__(self, title):
        self.title = title
    def __str__(self):
        return self.title