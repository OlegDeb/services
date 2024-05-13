from django.shortcuts import render
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'main/home.html'

class Company(TemplateView):
    template_name = 'main/company.html'
