from django.shortcuts import render, redirect, get_object_or_404
from .models import Carrinho, CupomDesconto, ItemCarrinho
from produto.models import Produto


def carrinho(request):
    cart = Carrinho.objects.get(id=Carrinho.objects.new_or_get(request).id)
    produtos = cart.produtos.all()
    cart.calculo_subtotal()
    return render(request, 'carrinho.html', {'carrinho': cart, 'produtos':produtos})

def change_qtd_item(request, item):
    cart = Carrinho.objects.get(id=request.session.get('cart_id'))
    produto = cart.produtos.get(id=item)
    produto.qtd = int(request.POST['qtd'])
    produto.save()
    cart.calculo_subtotal()
    return redirect('cart')

def deletar_carrinho(request):
    Carrinho.objects.deletar_carrinho(id_cart=request.session('cart_id'))
    return redirect('cart')

def remove_item_in_cart(request,item):
    cart = Carrinho.objects.new_or_get(request)
    cart.produtos.filter(id=item).delete()
    cart.save()
    return redirect('cart')

def aplicar_cupom(request):
    promo_code = request.POST['promo-code'] or None
    if promo_code != None:
        promo_code = get_object_or_404(CupomDesconto,titulo=promo_code)
        cart = Carrinho.objects.get(id=request.session.get('cart_id'))
        cart.cupom = promo_code
        cart.save()
        cart.aplicar_cupom()

    return redirect('cart')

def remover_cupom(request,cupom):
    Carrinho.objects.filter(cupom__id=cupom).update(cupom='')
    Carrinho.objects.calculo_subtotal()
    return redirect('cart')

def add_to_cart(request,item, qtd):
    qtd==1
    item_cart = ItemCarrinho.objects.create(produto=get_object_or_404(Produto, id=item),qtd=qtd)
    cart = Carrinho.objects.new_or_get(request)
    cart.produtos.add(item_cart)
    cart.save()
    

    return redirect('loja_home')

