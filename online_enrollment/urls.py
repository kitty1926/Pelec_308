from django.urls import path
from . import views

urlpatterns = [
    # Authentication URLs
    path("", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),
    
    # Dashboard (Protected)
    path("dashboard/", views.dashboard_view, name="dashboard"),
    
    # Student URLs (Protected)
    path("students/", views.students, name="students"),
    path("students/add/", views.add_student, name="add_student"),
    path("students/edit/<int:id>/", views.edit_student, name="edit_student"),
    path("students/delete/<int:id>/", views.delete_student, name="delete_student"),
    
    # Student Information URLs (Protected)
    path("student-information/", views.student_Information, name="student_information"),
    path("student-information/add/", views.add_student_information, name="add_student_information"),
    path("student-information/edit/<int:id>/", views.edit_student_info, name="edit_student_information"),
    path("student-information/delete/<int:id>/", views.delete_student_info, name="delete_student_information"),

    # Department URLs (Protected)
    path("departments/", views.department, name="departments"),
    path("departments/add/", views.add_department, name="add_department"),
    path("departments/edit/<int:id>/", views.edit_department, name="edit_department"),
    path("departments/delete/<int:id>/", views.delete_department, name="delete_department"),
    
    # Schedule URLs (Protected)
    path("schedules/", views.schedule, name="schedules"),
    path("schedules/add/", views.add_schedule, name="add_schedule"),
    path("schedules/edit/<int:id>/", views.edit_schedule, name="edit_schedule"),
    path("schedules/delete/<int:id>/", views.delete_schedule, name="delete_schedule"),
    
    # Classroom URLs (Protected)
    path("classrooms/", views.classroom, name="classrooms"),
    path("classrooms/add/", views.add_classroom, name="add_classroom"),
    path("classrooms/edit/<int:id>/", views.edit_classroom, name="edit_classroom"),
    path("classrooms/delete/<int:id>/", views.delete_classroom, name="delete_classroom"),
]