from django.urls import path
from .views import carrinho


urlpatterns = [
    path('cart/', carrinho, name='cart'),
]
