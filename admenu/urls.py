from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.admininfo_home, name='admininfo_home'),
    path('create_admininfo', views.create_admininfo, name='create_admininfo'),
    path('<int:pk>/update', views.admininfoUpdateView.as_view(), name='admininfo-update'),
    path('<int:pk>/delete', views.admininfoDeleteView.as_view(), name='admininfo-delete')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
