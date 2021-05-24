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
        order = Order.objects.create_order(Carrinho.objects.get(id=self.request.session.get('cart_id')))
        pg = order.pagseguro()
        print(order)

        return pg['redirect_url']
    

@csrf_exempt
def pagseguro_notification(request):
    code = request.POST.get('notificationCode', None)    
    return HttpResponse(code)


def detail_order(request):
    code1 = request.POST.get('id_transaction',None)
    code2 = request.GET.get('id_transaction',None)
    print(code1, code2)

    return render(request, 'order_detail.html')

        
    

