from django.db import models
from django.db.models import  Sum, F, FloatField
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

    def deletar_carrinho(self,id_cart):
        self.model.objects.get(id=id_cart).delete()
   
class CupomDesconto(models.Model):
    owner =  models.OneToOneField(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=30)
    valor = models.FloatField(default=0)

    def  __str__(self):
        return str(self.titulo) + ' ' + str(self.valor)

class ItemCarrinho(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE,blank=True, null=True)
    qtd = models.IntegerField(default=0)
    total_por_item = models.FloatField(default=0)

    def __str__(self):
        return  f' {self.id} PRODUTO:{self.produto} QTD:{self.qtd} TOTAL:{self.total_por_item}'

    def total_item(self):
        try:
            total = self.produto.preco * self.qtd
            ItemCarrinho.objects.filter(id=self.id).update(total_por_item=total)
        except:
            return None
     

#Mecher no subotoal e criar uma variavel total
class Carrinho(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    produtos = models.ManyToManyField(ItemCarrinho,  blank=True)
    subtotal = models.FloatField(default=0.00)
    total = models.FloatField(default=0.00)
    cupom = models.OneToOneField(CupomDesconto, on_delete=models.CASCADE, blank=True, null=True)
    
    objects = CartManager()
#TODO:ajeiar o calculo do total
    def calculo_subtotal(self):
        subtotal = self.produtos.all().aggregate(Sum('total_por_item'))['total_por_item__sum']
        if subtotal == None:
            subtotal = 0.00
        if subtotal <= 0:
            Carrinho.objects.update(subtotal=0.00)
        else:
            if self.cupom:
                total = subtotal - self.cupom.valor
                Carrinho.objects.update(subtotal=float(subtotal), total=float(total))
            else:
                Carrinho.objects.update(subtotal=float(subtotal), total=float(subtotal))
                
    def aplicar_cupom(self):
        self.calculo_subtotal()

    def __str__(self):
        return str(self.id )+ '  ' + str(self.user)

#TODO:Corrigir o valor total: Valor antes do descnto e depois do desconto

#TODO:Melhorar a função de remover um item especifico do carrinho.

@receiver(post_save, sender=ItemCarrinho)
def calculo_item(sender, instance, **kwargs):
    instance.total_item() 
#TODO:Possibilidade de remove sginals de post_delete do item carrinho.
@receiver(post_delete, sender=ItemCarrinho)
def deletar_item(sender, instance, **kwargs):
    instance.total_item() 

@receiver(post_delete, sender=Carrinho.produtos.through)
def deletar_item_cart(sender, instance, **kwargs):
    instance.calculo_subtotal()

@receiver(post_save, sender=Carrinho.produtos.through)
def add_item_cart(sender, instance, **kwargs):
    instance.calculo_subtotal()
  
@receiver(m2m_changed, sender=Carrinho.produtos.through)
def add_item_cart(sender, instance, **kwargs):
    instance.calculo_subtotal()
  
  
