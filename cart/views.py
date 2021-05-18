from django.shortcuts import render
from .models import Carrinho



# Create your views here.

def carrinho(request):
    if (Carrinho.objects.new_or_get(request)):
        message = 'carrinho já criado'
    
    

    return render(request, 'carrinho.html', {'message': message})