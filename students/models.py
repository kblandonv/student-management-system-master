from django.db import models


# Create your models here.
class Student(models.Model):
  """
  Represents a student in the student management system.

  Attributes:
    student_number (int): The student's unique identification number.
    first_name (str): The student's first name.
    last_name (str): The student's last name.
    email (str): The student's email address.
    field_of_study (str): The student's field of study.
    gpa (float): The student's grade point average.
  """

  student_number = models.PositiveIntegerField()
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.EmailField(max_length=100)
  field_of_study = models.CharField(max_length=50)
  gpa = models.FloatField()

  def __str__(self):
    return f'Student: {self.first_name} {self.last_name}'
