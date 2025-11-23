from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, StudentInformation, Department, Schedule, Classroom
from .forms import StudentForm, RegisterForm, LoginForm, StudentInformationForm, ClassroomForm, ScheduleForm, DepartmentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Authentication Views
def register_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registerd Succesfully!, Please Login.")
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "online_enrollment/register.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username / password.")
    else:
        form = LoginForm()
    return render(request, "online_enrollment/login.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect("login")


# Dashboard View (Protected)
@login_required(login_url='login')
def dashboard_view(request):
    return render(request, "online_enrollment/dashboard.html")


# Student Views (All Protected)
@login_required(login_url='login')
def students(request):
    student = Student.objects.all()
    return render(request, "online_enrollment/student_list.html", {"students": student})


@login_required(login_url='login')
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Added successfully")
            return redirect('students')
    else:
        form = StudentForm()
    return render(request, 'online_enrollment/add_student.html', {'form': form})

    
@login_required(login_url='login')
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated successfully!")
            return redirect('students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'online_enrollment/edit_student.html', {'form': form, 'student': student})


@login_required(login_url='login')
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    messages.success(request, "Deleted successfully!")
    return redirect('students')


# Student Information Views (All Protected)
@login_required(login_url='login')
def student_Information(request):
    students_info = StudentInformation.objects.all()
    return render(request, "online_enrollment/student_info_list.html", {"students_info": students_info})


@login_required(login_url='login')
def add_student_information(request):
    if request.method == "POST":
        form = StudentInformationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Students information have been added")
            return redirect('student_information')
    else:
        form = StudentInformationForm()
    return render(request, 'online_enrollment/add_student_info.html', {'form': form})


@login_required(login_url='login')
def edit_student_info(request, id):
    student_info = get_object_or_404(StudentInformation, id=id)
    if request.method == 'POST':
        form = StudentInformationForm(request.POST, instance=student_info)
        if form.is_valid():
            form.save()
            messages.success(request, "Students Information have been updated")
            return redirect('student_information')
    else:
        form = StudentInformationForm(instance=student_info)
    return render(request, 'online_enrollment/edit_student_info.html', {'form': form, 'student_info': student_info})


@login_required(login_url='login')
def delete_student_info(request, id):
    student_info = get_object_or_404(StudentInformation, id=id)
    student_info.delete()
    messages.success(request, "Students information have been deleted")
    return redirect('student_information')


# Department Views (All Protected)
@login_required(login_url='login')
def department(request):
    departments = Department.objects.all()
    return render(request, "online_enrollment/department_list.html", {"departments": departments})


@login_required(login_url='login')
def add_department(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Department has beeen added")
            return redirect('departments')
    else:
        form = DepartmentForm()
    return render(request, 'online_enrollment/add_department.html', {'form': form})


@login_required(login_url='login')
def edit_department(request, id):
    dept = get_object_or_404(Department, id=id)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=dept)
        if form.is_valid():
            form.save()
            messages.success(request, "Department has been updated")
            return redirect('departments')
    else:
        form = DepartmentForm(instance=dept)
    return render(request, 'online_enrollment/edit_department.html', {'form': form, 'department': dept})


@login_required(login_url='login')
def delete_department(request, id):
    dept = get_object_or_404(Department, id=id)
    dept.delete()
    messages.success(request, "Department has been deleted")
    return redirect('departments')


# Schedule Views (All Protected)
@login_required(login_url='login')
def schedule(request):
    schedules = Schedule.objects.all()
    return render(request, "online_enrollment/schedule_list.html", {"schedules": schedules})


@login_required(login_url='login')
def add_schedule(request):
    if request.method == "POST":
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Schedule has been added")
            return redirect('schedules')
    else:
        form = ScheduleForm()
    return render(request, 'online_enrollment/add_schedule.html', {'form': form})


@login_required(login_url='login')
def edit_schedule(request, id):
    sched = get_object_or_404(Schedule, id=id)
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=sched)
        if form.is_valid():
            form.save()
            messages.success(request, "Schedule has been updated")
            return redirect('schedules')
    else:
        form = ScheduleForm(instance=sched)
    return render(request, 'online_enrollment/edit_schedule.html', {'form': form, 'schedule': sched})


@login_required(login_url='login')
def delete_schedule(request, id):
    sched = get_object_or_404(Schedule, id=id)
    sched.delete()
    messages.success(request, "Schedule has been deleted")
    return redirect('schedules')


# Classroom Views (All Protected)
@login_required(login_url='login')
def classroom(request):
    classrooms = Classroom.objects.all()
    return render(request, "online_enrollment/classroom_list.html", {"classrooms": classrooms})


@login_required(login_url='login')
def add_classroom(request):
    if request.method == "POST":
        form = ClassroomForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Classroom has been added ")
            return redirect('classrooms')
    else:
        form = ClassroomForm()
    return render(request, 'online_enrollment/add_classroom.html', {'form': form})


@login_required(login_url='login')
def edit_classroom(request, id):
    room = get_object_or_404(Classroom, id=id)
    if request.method == 'POST':
        form = ClassroomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            messages.success(request, "Classroom has been updated")
            return redirect('classrooms')
    else:
        form = ClassroomForm(instance=room)
    return render(request, 'online_enrollment/edit_classroom.html', {'form': form, 'classroom': room})


@login_required(login_url='login')
def delete_classroom(request, id):
    room = get_object_or_404(Classroom, id=id)
    room.delete()
    messages.success(request, "Classroom has been deleted")
    return redirect('classrooms')