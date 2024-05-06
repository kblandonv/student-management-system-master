from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
  """
  A form for creating or updating a student.

  This form is used to collect and validate data for the `Student` model.
  It provides a set of fields and widgets to render the form in HTML.

  Attributes:
    model (class): The model class associated with the form.
    fields (list): The fields to include in the form.
    labels (dict): The labels to use for the form fields.
    widgets (dict): The widgets to use for the form fields.

  Example:
    form = StudentForm()
    if form.is_valid():
      form.save()
  """

  class Meta:
    model = Student
    fields = ['student_number', 'first_name', 'last_name', 'email', 'field_of_study', 'gpa']
    labels = {
      'student_number': 'Student Number',
      'first_name': 'First Name',
      'last_name': 'Last Name',
      'email': 'Email',
      'field_of_study': 'Field of Study',
      'gpa': 'GPA'
    }
    widgets = {
      'student_number': forms.NumberInput(attrs={'class': 'form-control'}),
      'first_name': forms.TextInput(attrs={'class': 'form-control'}),
      'last_name': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'field_of_study': forms.TextInput(attrs={'class': 'form-control'}),
      'gpa': forms.NumberInput(attrs={'class': 'form-control'}),
    }
