from django.urls import path
from .views import LojaHome


urlpatterns = [
    path('', LojaHome.as_view(), name='loja_home'),
    
]
