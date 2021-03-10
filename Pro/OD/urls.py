from django.urls import path
from . import views

app_name = 'OD'

urlpatterns = [
    path('',views.odlist,name = 'OD_list'),
]