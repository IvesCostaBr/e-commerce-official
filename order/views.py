from django.shortcuts import render, redirect
from django.views.generic import TemplateView
import requests

class Chekout(TemplateView):
    template_name = 'checkout.html'
