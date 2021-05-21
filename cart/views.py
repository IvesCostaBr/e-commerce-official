from django.shortcuts import render, redirect
from .models import Carrinho, ItemCarrinho

# Create your views here.

def carrinho(request):
    cart = Carrinho.objects.get(id=Carrinho.objects.new_or_get(request).id)
    produtos = cart.produtos.all()
    return render(request, 'carrinho.html', {'carrinho': cart, 'produtos':produtos})


#TODO:pensar possibilidades
def remove_item(request, item):
    cart = Carrinho.objects.get(id=request.session.get('cart_id'))
    produto = cart.produtos.get(id=item)
    produto.qtd = int(request.POST['qtd'])
    produto.save()
    Carrinho.objects.calculo_subtotal()
    return redirect('cart')

def deletar_carrinho(request):
    Carrinho.objects.deletar_carrinho(id_cart=request.session('id_cart'))
    return redirect('cart')
