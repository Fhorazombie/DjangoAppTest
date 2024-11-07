import os
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Client
from .serializers import ClientSerializer
import requests

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

@api_view(['GET'])
def module2_view(request):
    return Response({"message": "This is Module 2"})

@api_view(['GET'])
def get_client(request):
    client = Client.objects.get(pk=1)
    serializer = ClientSerializer(client)
    return Response(serializer.data)

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'module2/client_list.html', {'clients': clients})