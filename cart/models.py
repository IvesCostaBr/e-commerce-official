from django.db import models
from django.conf import settings
from produto.models import Produto
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver


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


class ItemPedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT ,blank=True, null=True)
    qtd = models.IntegerField(default=0)
    total_por_item = models.FloatField(default=0)

    def __str__(self):
        return f'Produto:{self.produto}   QTD:{self.qtd}  {self.total_por_item}'

    def total_item(self):
        total = self.produto.preco * self.qtd
        ItemPedido.objects.filter(id=self.id).update(total_por_item=total)


class Carrinho(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    produtos = models.ManyToManyField(ItemPedido,  blank=True)
    subtotal = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True, default=0.00)

    objects = CartManager()

    def calculo_subtotal(self):
        total = 0
        items = self.produtos.all()
        for c in range(items.count()):
            total = total + items[c].total_por_item

        print('entrou no canculo')

        Carrinho.objects.update(subtotal=total)
    
    def __str__(self):
        return str(self.id )+ '  ' + str(self.user)



@receiver(post_save, sender=ItemPedido)
def calculo_item(sender, instance, **kwargs):
    instance.total_item() 

@receiver(m2m_changed ,sender=Carrinho.produtos.through)
def calculo_subotal(sender, instance, **kwargs):
    instance.calculo_subtotal()

  
  
