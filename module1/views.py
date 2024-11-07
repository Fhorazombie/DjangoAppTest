import os
from django.shortcuts import render, redirect
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Company
from .serializers import CompanySerializer
from .forms import CompanyForm
import requests

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        data['clients'] = serializer.get_clients(instance)
        return Response(data)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            data = serializer.data
            for company in data:
                company['clients'] = self.get_serializer().get_clients(Company.objects.get(id=company['id']))
            return self.get_paginated_response(data)

        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        for company in data:
            company['clients'] = self.get_serializer().get_clients(Company.objects.get(id=company['id']))
        return Response(data)

@api_view(['GET'])
def get_company(request):
    company = Company.objects.get(pk=1)
    serializer = CompanySerializer(company)
    return Response(serializer.data)

def company_list(request):
    companies = Company.objects.all()
    return render(request, 'module1/company_list.html', {'companies': companies})

def company_create(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company-list')
    else:
        form = CompanyForm()
    return render(request, 'module1/company_create.html', {'form': form})

@api_view(['POST'])
def company_create_api(request):
    serializer = CompanySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    data = serializer.data
    for company in data:
        company['clients'] = serializer.get_clients(Company.objects.get(id=company['id']))
    return render(request, 'module1/company_list.html', {'companies': data})