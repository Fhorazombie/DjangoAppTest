import os
from django.shortcuts import render, redirect
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Client
from .serializers import ClientSerializer
from .forms import ClientForm
import requests

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
    # Fetch company data from API
    api_url = os.environ.get('COMPANY_API_URL', 'http://localhost:8000/module1/api/get-companies')
    try:
        response = requests.get(api_url)
        companies = response.json()
    except requests.RequestException:
        companies = []

    if request.method == 'POST':
        form = ClientForm(request.POST, companies=companies)
        if form.is_valid():
            form.save()
            return redirect('client-list')
    else:
        form = ClientForm(companies=companies)

    return render(request, 'module2/create_client.html', {'form': form, 'companies': companies})