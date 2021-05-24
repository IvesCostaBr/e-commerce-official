from django.urls import path
from .views import Chekout, Pagseguro, pagseguro_notification


urlpatterns = [
    path('', Chekout.as_view(), name='checkout'),
    path('finalizando/pagseguro/', Pagseguro.as_view(), name='pagseguro_payment'),
    path('receiver-pagseguro/', pagseguro_notification),
]
