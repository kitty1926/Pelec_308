from django import forms
from .models import Student, StudentInformation, Classroom, Schedule, Department
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id','first_name','last_name','course','lrn']

class StudentInformationForm(forms.ModelForm):
    class Meta:
        model = StudentInformation
        fields = ['contact_no','email','address','last_year_attended','date_of_birth']


class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = '__all__'

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

