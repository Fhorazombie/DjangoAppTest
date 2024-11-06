from django.urls import path
from . import views

urlpatterns = [
    path('', views.module1_view, name='module1_view'),
]