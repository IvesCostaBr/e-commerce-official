from django.contrib import admin
from django.urls import path, include
from cart import urls as cart_urls
from loja import urls as loja_urls
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include(cart_urls)),
    path('', include(loja_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
