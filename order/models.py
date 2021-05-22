from django.db import models
from django.contrib.auth.models import User
from cart.models import ItemCarrinho

# Create your models here.


class Order(models.Model):
    comprador = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=12,default='Em processamento')
    cod_pagamento = models.CharField(max_length=14,blank=True, null=True)
    valor_total = models.FloatField(default=0.00)

    def __str__(self):  
        return self.comprador 