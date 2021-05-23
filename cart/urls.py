from django.urls import path, include
from .views import (carrinho, 
change_qtd_item,  
deletar_carrinho, 
remove_item_in_cart, 
aplicar_cupom,
remover_cupom,
add_to_cart,
)
from order import urls as order_urls


urlpatterns = [
    path('', carrinho, name='cart'),
    path('change_qtd/<int:item>/', change_qtd_item, name='change_qtd'),
    path('adicionar_cupom/', aplicar_cupom, name='adicionar_cupom'), 
    path('remove_item/<int:item>/',remove_item_in_cart, name='remove_item'),
    path('remover_cupom/<int:cupom>/', remover_cupom, name='cupom_remove'),
    path('add_to_cart/<int:item>/<int:qtd>/', add_to_cart, name='add_to_cart'),
    path('chekout', include(order_urls)),

   
]
