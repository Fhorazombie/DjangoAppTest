import os
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Company
from .serializers import CompanySerializer
import requests

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

@api_view(['GET'])
def module1_view(request):
    return Response({"message": "This is Module 1"})

@api_view(['GET'])
def get_clients(request):
    module2_url = os.environ.get('MODULE2_URL', 'http://localhost:8001')
    response = requests.get(f'{module2_url}/api/clients/')
    if response.status_code == 200:
        return Response(response.json())
    return Response({"error": "Unable to fetch clients"}, status=status.HTTP_503_SERVICE_UNAVAILABLE)