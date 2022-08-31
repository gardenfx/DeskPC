from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.users_home, name='users_home'),
    path('create', views.create, name='create'),
    path('<int:pk>/update', views.UsersUpdateView.as_view(), name='users-update'),
    path('<int:pk>/delete', views.UsersDeleteView.as_view(), name='users-delete'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
