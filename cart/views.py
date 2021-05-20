from django.shortcuts import render
from .models import Carrinho



# Create your views here.

def carrinho(request):
    cart = Carrinho.objects.get(id=Carrinho.objects.new_or_get(request).id)
    
    return render(request, 'carrinho.html', {'carrinho': cart})