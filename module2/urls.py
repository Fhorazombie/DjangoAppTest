from django.urls import path
from . import views

urlpatterns = [
    path('', views.module2_view, name='module2_view'),
]