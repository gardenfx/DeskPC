from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.PC_home, name='map_grid'),
    path('create', views.addPC, name='addPC'),
    path('<int:pk>/update', views.PCUpdateView.as_view(), name='PC-update'),
    path('<int:pk>/delete', views.PCDeleteView.as_view(), name='PC-delete')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
