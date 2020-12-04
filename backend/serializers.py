from rest_framework import serializers
from backend.models import FetchedData


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = FetchedData
        fields = ['data_id', 'data_name', 'data_time', 'data_json']
