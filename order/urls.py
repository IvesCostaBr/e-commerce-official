from django.urls import path
from .views import Chekout


urlpatterns = [
    path('', Chekout.as_view(), name='checkout'),
]
