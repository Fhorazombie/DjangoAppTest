from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'companies', views.CompanyViewSet)

urlpatterns = [
    path('', views.company_list, name='company-list'),
    path('api/get-companies', views.get_company, name='get-companies'),
    path('company-create/', views.company_create, name='company-create'),
    path('api/company-create/', views.company_create_api, name='company-create-api'),
]