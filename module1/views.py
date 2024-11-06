from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Company
from .serializers import CompanySerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

def module1_view(request):
    return HttpResponse("This is Module 1")