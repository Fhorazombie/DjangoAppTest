from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'companies', views.CompanyViewSet)

urlpatterns = [
    path('', views.company_list, name='company-list'),
    path('module1/', views.module1_view, name='module1'),
    path('get-company/', views.get_company, name='get-company'),
    path('company-list/', views.company_list, name='company-list'),
]