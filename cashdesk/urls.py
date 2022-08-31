from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.cashdesk_shop, name='cashdesk'),
    path('addMoneyPhone', views.addMoneyPhone, name='addMoneyPhone'),
    path('venue_pdf', views.venue_pdf, name='venue_pdf')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
