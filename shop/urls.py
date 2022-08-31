from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.shop_home, name='shop_home'),
    path('create_shop', views.create_shop, name='create_shop'),
    path('<int:pk>/update', views.ShopUpdateView.as_view(), name='shop-update'),
    path('<int:pk>/delete', views.ShopDeleteView.as_view(), name='shop-delete')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
