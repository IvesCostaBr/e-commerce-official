from django.urls import path
from .views import carrinho, remove_item


urlpatterns = [
    path('cart/', carrinho, name='cart'),
    path('change_atd/<int:item>/', remove_item, name='change_qtd'),
]
