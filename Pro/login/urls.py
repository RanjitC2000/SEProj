from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('student/',views.slogin,name = 'student_login'),
    path('faculty/',views.flogin,name = 'faculty_login'),
]