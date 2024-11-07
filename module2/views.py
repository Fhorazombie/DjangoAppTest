import os
from django.shortcuts import render, redirect
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Client
from .serializers import ClientSerializer
from .forms import ClientForm
import requests
from module1.models import Company
from django.shortcuts import get_object_or_404, redirect, render

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

@api_view(['GET'])
def get_clients(request):
    clients = Client.objects.all()
    serializer = ClientSerializer(clients, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_clients_byid(request):
    company_id = request.GET.get('id')
    clients = Client.objects.filter(company=company_id)
    serializer = ClientSerializer(clients, many=True)
    return Response(serializer.data)


def client_list(request):
    clients = Client.objects.all()
    return render(request, 'module2/client_list.html', {'clients': clients})

def create_client(request):
    # Obtén todas las compañías para pasar como choices al formulario
    companies = Company.objects.all()

    if request.method == 'POST':
        form = ClientForm(request.POST, companies=companies)
        if form.is_valid():
            client = form.save(commit=False)
            # Obtener el ID de la compañía y buscar la instancia de Company
            company_id = form.cleaned_data['company']
            print(f"company_id: {company_id}, type: {type(company_id)}")
            company_instance = get_object_or_404(Company, id=company_id)
            client.company = company_instance
            client.save()
            return redirect('client-list')
    else:
        form = ClientForm(companies=companies)

    return render(request, 'module2/create_client.html', {'form': form, 'companies': companies})