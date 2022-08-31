from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.kniga_ucheta_home, name='knig_uchet_home'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
