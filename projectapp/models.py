from django.db import models


class Course(models.Model):
    """
    The course model contains basic info on the course and semester and will be
    linked to relevant professors and projects
    """
    # Descriptive name of the course
    name = models.CharField(max_length=100, default='')
    # Course abbreviation with spaces, i.e. M E 369P
    abbreviation = models.CharField(max_length=50, default='')
    # Course semester and year with a space, i.e. Spring 2020
    semester = models.CharField(max_length=50, default='')
    # Name of page defined in urls.py
    view_page = 'course_page_link'
    def get_link(self):
        """
        Returns the string used in referencing the object through urls
        """
        abbreviation_no_spaces = self.abbreviation.replace(' ','')
        semester_no_spaces = self.semester.replace(' ','')
        # Returns the course abbreviation and semester with an underscore and no spaces, i.e. ME369P_Spring2020
        return abbreviation_no_spaces + '_' + semester_no_spaces
    def __str__(self):
        return self.name + ', ' + self.semester


class Student(models.Model):
    """
    The student model contains basic info on the student and will be linked to 
    relevant projects
    """
    # First and last name of the student
    name = models.CharField(max_length=100, default='')
    # Eid of the student
    eid = models.CharField(max_length=50, default='')
    # Name of page defined in urls.py
    view_page = 'student_page_eid'
    def get_link(self):
        """
        Returns the string used in referencing the object through urls
        """
        return self.eid
    def __str__(self):
        return self.name


class Professor(models.Model):
    """
    The professor model contains basic info on the professor and will be linked 
    to relevant courses
    """
    # First and last name of the professor with title, i.e. Dr. Mitchell Pryor
    name = models.CharField(max_length=100, default='')
    # Eid of the student
    eid = models.CharField(max_length=50, default='')
    # Many to many field referencing relevant courses
    courses_raw = models.CharField(max_length=100, default='')
    courses = models.ManyToManyField(Course)
    # Name of page defined in urls.py
    view_page = 'professor_page_eid'
    def get_link(self):
        """
        Returns the string used in referencing the object through urls
        """
        return self.eid
    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    The tag model contains basic info on the tag and will be linked to relevant 
    projects
    """
    # Name of the tag
    name = models.CharField(max_length=100, default='')
    def __str__(self):
        return self.name


class Project(models.Model):
    # Descriptive name of the project
    name = models.CharField(max_length=100, default='')
    # Many to many field referencing relevant courses
    course_raw = models.CharField(max_length=100, default='')
    course = models.ManyToManyField(Course)
    # Many to many field referencing relevant students
    students_raw = models.CharField(max_length=100, default='')
    students = models.ManyToManyField(Student)
    # Many to many field referencing relevant professors
    professors_raw = models.CharField(max_length=100, default='')
    professors = models.ManyToManyField(Professor)
    # Many to many field referencing relevant tags
    tags_raw = models.CharField(max_length=100, default='')
    tags = models.ManyToManyField(Tag)
    # Long summary of the project
    summary = models.CharField(max_length=100, default='')
    # Reference to image
    image_raw = models.CharField(max_length=100, default='')
    image = models.ImageField()
    # Link to relevant resources
    link = models.CharField(max_length=100, default='')
    # Name of page defined in urls.py
    view_page = 'project_page_id'
    def get_link(self):
        """
        Returns the string used in referencing the object through urls
        """
        return self.id
    def __str__(self):
        return self.name
