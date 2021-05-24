from django.urls import path, include
from .views import LojaHome
from costumer import urls as costume_url


urlpatterns = [
    path('', LojaHome.as_view(), name='loja_home'),
    path('my-account/', include(costume_url)),
    
]
