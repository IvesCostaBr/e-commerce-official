from django.urls import path
from .views import Chekout, Pagseguro, pagseguro_notification



urlpatterns = [
    path('checkout/', Chekout.as_view(), name='checkout'),
    path('finalizando/<int:id>/pagseguro/', Pagseguro.as_view(), name='pagseguro_payment'),
    path('pagseguro_notification/',pagseguro_notification)
] 