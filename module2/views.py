from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Client
from .serializers import ClientSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

def module2_view(request):
    return HttpResponse("This is Module 2")