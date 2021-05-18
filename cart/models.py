from django.db import models
from django.conf import settings
from produto.models import Produto
from django.contrib.auth.models import User




class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id")
        qs = self.get_queryset().filter(id = cart_id)
        if qs.count() == 1:
            cart_obj = qs.first()
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()  
        else:
            cart_obj = Carrinho.objects.new(user = request.user)
            request.session['cart_id'] = cart_obj.id
        return cart_obj

    def new(self, user = None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user = user_obj)


class Carrinho(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    produtos = models.ForeignKey(Produto, on_delete=models.CASCADE, blank=True, null=True)
    subtotal = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id )+ '  ' + str(self.user)