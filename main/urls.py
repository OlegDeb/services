from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('company', Company.as_view(), name='company'),
]

