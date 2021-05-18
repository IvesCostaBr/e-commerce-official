from django.contrib import admin
from django.urls import path, include
from cart import urls as cart_urls



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(cart_urls)),
]
