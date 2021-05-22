from django.contrib import admin
from .models import Carrinho, ItemCarrinho, CupomDesconto

# Register your models here.

admin.site.register(Carrinho)
admin.site.register(ItemCarrinho)
admin.site.register(CupomDesconto)