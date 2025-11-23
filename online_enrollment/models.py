# models.py

from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    lrn = models.CharField(max_length=100)
    def __str__(self):
            return f"{self.first_name}"

class StudentInformation(models.Model):
    contact_no = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    last_year_attended = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    def __str__(self):
            return f"{self.email}"

class Department(models.Model):
    department_name = models.CharField(max_length=100)
    head_of_department = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=100)
    def __str__(self):
            return f"{self.department_name}"

class Schedule(models.Model):
    time_slot = models.CharField(max_length=100)
    day_of_week = models.CharField(max_length=100)
    student_room = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    student_id = models.CharField(max_length=100)
    def __str__(self):
            return f"{self.day_of_week}"

class Classroom(models.Model):
    building_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    course_id = models.CharField(max_length=100)
    day_of_week = models.CharField(max_length=100)
    time_slot = models.CharField(max_length=100)    

    def __str__(self):
            return f"{self.building_name}"


# Create your models here.
