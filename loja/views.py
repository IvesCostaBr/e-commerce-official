from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from produto.models import Produto
from cart.models import ItemCarrinho, Carrinho


# Create your views here.

class LojaHome(TemplateView):
    template_name = 'loja.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Carrinho.objects.new_or_get(self.request)
        context['produtos'] = Produto.objects.all()
        return context


