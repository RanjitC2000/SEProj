from django.contrib import admin
from .models import ODList

admin.site.register(ODList, verbose_name='ODs')
# Register your models here.
