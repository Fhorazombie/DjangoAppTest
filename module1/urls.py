from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'companies', views.CompanyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('module1/', views.module1_view, name='module1'),
    path('get-clients/', views.get_clients, name='get-clients'),
]