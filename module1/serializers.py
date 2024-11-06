from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.ModelSerializer):
    clients = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Company
        fields = '__all__'