from django.contrib import admin
from .models import Student,Faculty

admin.site.register([Student,Faculty], verbose_name=['Students','Faculties'])

# Register your models here.
