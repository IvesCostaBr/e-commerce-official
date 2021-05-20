from django.contrib import admin
from .models import Carrinho, ItemPedido

# Register your models here.

admin.site.register(Carrinho)
admin.site.register(ItemPedido)