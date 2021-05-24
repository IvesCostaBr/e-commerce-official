from django import conf
from django.db import models
from django.conf import settings
from cart.models import ItemCarrinho
from pagseguro.api import PagSeguroItem, PagSeguroApi
from pagseguro.signals import notificacao_recebida
import uuid



# Create your models here.


def generate_code():
    return uuid.uuid4()


class Order(models.Model):
    STATUS_CHOICES = (
        (0,'Aguardando Pagamento'),
        (1,'Pagamento Aprovado'),
        (2,'Em separação'),
        (3,'Concluida'),
        (4,'Cancelada'),
    )
    PAYMENT_OPTION_CHOICES = (
        ('deposit', 'Depósito'),
        ('pagseguro', 'PagSeguro'),
        ('paypal', 'PayPal')
    )
    id = models.UUIDField(primary_key=True, editable=False, default=generate_code)
    comprador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    status = models.IntegerField('Situação', choices=STATUS_CHOICES, default=0, blank=True)
    payment_method = models.CharField('opção de pagamento', choices=PAYMENT_OPTION_CHOICES, max_length=20, default='deposit')
    all_produtos = models.ManyToManyField(ItemCarrinho, blank=True)
    cod_pagamento = models.CharField(max_length=30,blank=True, null=True)
    valor_total = models.FloatField(default=0.00)

    def __str__(self):
        return str(self.id) + ' '+ str(self.comprador)

    def pagseguro(self):
        pagseguro_api = PagSeguroApi(reference=self.id)
        for item in self.all_produtos.all():
            item = PagSeguroItem(
                    id=item.produto.id, 
                    description=item.produto.titulo, 
                    amount = item.produto.preco, 
                    quantity =item.qtd
        )
            pagseguro_api.add_item(item)
           
    
        return pagseguro_api.checkout()


def update_purchase_status(sender, transaction, **kwargs):
    print('pedido atualizado')


notificacao_recebida.connect(update_purchase_status)