from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.ModelSerializer):
    clients = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = '__all__'

    def get_clients(self, obj):
        from module2.serializers import ClientSerializer
        return ClientSerializer(obj.clients.all(), many=True).data