from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('users/', include('users.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('map-grid/', include('mapgrid.urls')),
    path('cashdesk/', include('cashdesk.urls')),
    path('shop/', include('shop.urls')),
    path('devices/', include('devices.urls')),
    path('admenu/', include('admenu.urls')),
    path('content/', include('content.urls')),
    path('rate/', include('rate.urls'))
]
