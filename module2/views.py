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
def get_companies(request):
    module1_url = os.environ.get('MODULE1_URL', 'http://localhost:8000')
    response = requests.get(f'{module1_url}/api/companies/')
    if response.status_code == 200:
        return Response(response.json())
    return Response({"error": "Unable to fetch companies"}, status=status.HTTP_503_SERVICE_UNAVAILABLE)