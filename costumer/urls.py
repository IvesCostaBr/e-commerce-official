from django.urls import path
from .views import HomeCostumer


urlpatterns = [
    path('', HomeCostumer.as_view(), name='my_account'),
]
