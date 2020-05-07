from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100, default='')
    abbreviation = models.CharField(max_length=50, default='')
    semester = models.CharField(max_length=50, default='')
    view_page = 'course_page_link'
    def get_link(self):
        abbreviation_no_spaces = self.abbreviation.replace(' ','')
        semester_no_spaces = self.semester.replace(' ','')
        return abbreviation_no_spaces + '_' + semester_no_spaces
    def __str__(self):
        return self.abbreviation + ' ' + self.semester


class Student(models.Model):
    name = models.CharField(max_length=100, default='')
    eid = models.CharField(max_length=50, default='')
    view_page = 'student_page_eid'
    def get_link(self):
        return self.eid
    def __str__(self):
        return self.name


class Professor(models.Model):
    name = models.CharField(max_length=100, default='')
    eid = models.CharField(max_length=50, default='')
    courses_raw = models.CharField(max_length=100, default='')
    courses = models.ManyToManyField(Course)
    view_page = 'professor_page_eid'
    def get_link(self):
        return self.eid
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, default='')
    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100, default='')
    course_raw = models.CharField(max_length=100, default='')
    course = models.ManyToManyField(Course)
    students_raw = models.CharField(max_length=100, default='')
    students = models.ManyToManyField(Student)
    professors_raw = models.CharField(max_length=100, default='')
    professors = models.ManyToManyField(Professor)
    tags_raw = models.CharField(max_length=100, default='')
    tags = models.ManyToManyField(Tag)
    summary = models.CharField(max_length=100, default='')
    image_raw = models.CharField(max_length=100, default='')
    image = models.ImageField()
    link = models.CharField(max_length=100, default='')
    view_page = 'project_page_id'
    def get_link(self):
        return self.id
    def __str__(self):
        return self.name
