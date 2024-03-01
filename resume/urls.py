from django.contrib import admin
from django.urls import path, include
from resume.views import *


app_name = 'resume'

urlpatterns = [
    path('', base_view, name='index'),
]