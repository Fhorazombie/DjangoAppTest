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
def get_company(request):
    company = Company.objects.get(pk=1)
    serializer = CompanySerializer(company)
    return Response(serializer.data)

def company_list(request):
    companies = Company.objects.all()
    return render(request, 'module1/company_list.html', {'companies': companies})