from django.db import models
from django.db.models import  Sum, FloatField
from django.conf import settings
from produto.models import Produto
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed, post_delete, post_save
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

    def calculo_subtotal(self):
        total = 0.00
        subtotal = self.model.produtos.through.itemcarrinho.get_queryset().aggregate(Sum('total_por_item'))['total_por_item__sum']
        if subtotal < 0:
            self.model.objects.update(subtotal=0.00)
        else:
            self.model.objects.update(subtotal=subtotal)

    def deletar_carrinho(self,id_cart):
        self.model.objects.get(id=id_cart).delete()
   


class ItemCarrinho(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE,blank=True, null=True)
    qtd = models.IntegerField(default=0)
    total_por_item = models.FloatField(default=0)

    def __str__(self):
        return  f' {self.id} PRODUTO:{self.produto} QTD:{self.qtd} TOTAL:{self.total_por_item}'

    def total_item(self):
        
        if self.qtd <= 0 or self.total_por_item <= 0:
            item = ItemCarrinho.objects.get(id=self.id)
            print(item)
            print(Carrinho.objects.get(produtos=self))
        
        total = self.produto.preco * self.qtd
        ItemCarrinho.objects.filter(id=self.id).update(total_por_item=total)

  

#TODO:Achar solução mais viavel (Metodo mais eficaz de calcular todo)

class Carrinho(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    produtos = models.ManyToManyField(ItemCarrinho,  blank=True)
    subtotal = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True, default=0.00)

    objects = CartManager()

    #def calculo_subtotal(self):
    #    total = 0.00
    #    qtd = self.produtos.values('total_por_item')[0]
    #    for c in  range(self.produtos.count):
    #        total = total + qtd['total_por_item']

    #    Carrinho.objects.update(subtotal=total)
    
    def __str__(self):
        return str(self.id )+ '  ' + str(self.user)



@receiver(post_save, sender=ItemCarrinho)
def calculo_item(sender, instance, **kwargs):
    instance.total_item() 

@receiver(post_delete, sender=ItemCarrinho)
def deletar_item(sender, instance, **kwargs):
    instance.total_item() 

@receiver(post_delete, sender=Carrinho.produtos.through)
def deletar_item(sender, instance, **kwargs):
    instance.calcular_subtotal()
  
