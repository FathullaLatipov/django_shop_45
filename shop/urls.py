from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path

from products.views import home_page, MyLoginView, logout_view, single_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home_page'),
    path('login', MyLoginView.as_view(), name='login'),
    path('logout', logout_view, name='logout'),
    path('product/<int:pk>', single_product, name='single-product')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
