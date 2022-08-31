from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='home'),
    path('map-grid', views.mapgrid, name='map_grid'),
    path('cashdesk', views.cashdesk, name='cashdesk'),
    path('shop', views.shop, name='shop'),
    path('devices', views.devices, name='devices'),
    path('content', views.content, name='content'),
    path('rate', views.rate, name='rate'),
    path('users', views.users, name='users'),
    path('admenu', views.admenu, name='admenu'),
    path('auth', views.auth, name='auth'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
