from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import login,logout

# Create your views here.
from . models import Student,Faculty

def slogin(request):
    if request.method == 'POST':
        values = request.POST
        flag = 1
        for i in range(len(Student.objects.all())):
            if(str(values['user']) == str(Student.objects.all()[i].username) and str(values['password']) == str(Student.objects.all()[i].password)):               
                flag = 0
                return render(request,'student_home.html')
        if flag:
            return render(request , 'login/error.html')
    else:
        return render(request, 'login/login.html')

def flogin(request):
    if request.method == 'POST':
        values = request.POST
        flag = 1
        for i in range(len(Faculty.objects.all())):
            if(str(values['user']) == str(Faculty.objects.all()[i].username) and str(values['password']) == str(Faculty.objects.all()[i].password)):               
                flag = 0
                return render(request,'faculty_home.html')
        if flag:
            return render(request , 'login/error.html')
    else:
        return render(request, 'login/login.html')

# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status

# from .models import Student
# from .serializers import *

# @api_view(['GET', 'POST'])
# def students_list(request):
#     if request.method == 'GET':
#         data = Student.objects.all()

#         serializer = StudentSerializer(data, context={'request': request}, many=True)

#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED)
#         if request.method == 'POST':
#         values = request.POST
#         flag = 1
#         for i in range(len(Student.objects.all())):
#             if(str(values['user']) == str(Student.objects.all()[i].username) and str(values['password']) == str(Student.objects.all()[i].password)):               
#                 flag = 0
#                 return render(request,'student_home.html')
#         if flag:
#             return render(request , 'login/error.html')
#         else:
#             return render(request, 'login/login.html')
            
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
