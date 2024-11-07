from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'clients', views.ClientViewSet)

urlpatterns = [
    path('', views.client_list, name='client-list'),
    path('api/get-clients/', views.get_clients, name='get-clients'),
    path('api/get-clients-byid/', views.get_clients_byid, name='get-clients-byid'),
    path('create/', views.create_client, name='create_client'),
]