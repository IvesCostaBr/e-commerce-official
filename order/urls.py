from django.urls import path
from .views import Chekout, Pagseguro



urlpatterns = [
    path('checkout/', Chekout.as_view(), name='checkout'),
    path('finalizando/<int:id>/pagseguro/', Pagseguro.as_view(), name='pagseguro_payment'),
] 