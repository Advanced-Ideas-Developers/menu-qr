from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.

class LasTejitasView(TemplateView):
    template_name = 'restaurants/las_tejitas.html'
