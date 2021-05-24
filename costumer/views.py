from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HomeCostumer(TemplateView):
    template_name = 'costumer_home.html'