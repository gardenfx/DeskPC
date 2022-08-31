from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.bron_home, name='bron_home'),
    path('create_bron', views.create_bron, name='create_bron'),
    path('<int:pk>/update', views.BronUpdateView.as_view(), name='bron-update'),
    path('<int:pk>/delete', views.BronDeleteView.as_view(), name='bron-delete')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
