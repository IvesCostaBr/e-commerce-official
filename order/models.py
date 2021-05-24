from django.db import models
from django.contrib.auth.models import User
from pagseguro.api import PagSeguroItem, PagSeguroApi
from django.conf import settings
from cart.models import ItemCarrinho
# Create your models here.


class Order(models.Model):
    comprador = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.BooleanField(default=0)
    all_produtos = models.ManyToManyField(ItemCarrinho, blank=True)
    cod_pagamento = models.CharField(max_length=14,blank=True, null=True)
    valor_total = models.FloatField(default=0.00)


    def pagseguro(self):
        pagseguro_api = PagSeguroApi(reference=f'#{self.id}')
        for item in self.all_produtos.all():
            item = PagSeguroItem(id=item.produto.id, description=item.produto.titulo, amount=item.produto.preco, quantity=item.qtd)
            pagseguro_api.add_item(item)
        data = pagseguro_api.checkout()
        return data

    def atualizar_status(self):
        pagseguro_api = PagSeguroApi()
        resultado = pagseguro_api.get_transaction(f'#{self.id}')
        print(resultado['success'])
        print(resultado)