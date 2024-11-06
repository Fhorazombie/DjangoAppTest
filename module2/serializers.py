from rest_framework import serializers
from .models import Client
from module1.serializers import CompanySerializer

class ClientSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    company_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Company.objects.all(), source='company')

    class Meta:
        model = Client
        fields = '__all__'