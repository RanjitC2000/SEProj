from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.
from . models import ODList

def odlist(request):
    return HttpResponse(1)

