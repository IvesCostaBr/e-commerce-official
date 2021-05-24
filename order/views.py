from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views.generic import TemplateView, RedirectView
from cart.models import Carrinho
from .models import Order
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

class Chekout(TemplateView):
    template_name = 'checkout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = get_object_or_404(Carrinho, id=self.request.session.get('cart_id'))

        return context

    


class Pagseguro(RedirectView):
    def get_redirect_url(self, *args, **kwargs): 
        cart = Carrinho.objects.get(id=self.request.session.get('cart_id'))
        order = Order.objects.create(
            comprador=cart.user,
            valor_total=cart.subtotal,
            )
        order.all_produtos.set(cart.produtos.all())
        cart.delete()
        pg = order.pagseguro()
        url = (pg['redirect_url'])
        return url


@csrf_exempt
def pagseguro_notification(request):
    code = request.POST['notificationCode' or None]
    print(code)
    
    return HttpResponse('OK')
