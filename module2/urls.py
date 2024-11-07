from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'clients', views.ClientViewSet)

urlpatterns = [
    path('', views.client_list, name='client-list'),
    path('get-clients/', views.get_clients, name='get-clients'),
    path('create/', views.create_client, name='create_client'),
]