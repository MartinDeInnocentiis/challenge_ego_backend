from rest_framework import serializers
from .models import Activity, Financing


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'name', 'description', 'datetime', 'address']
        

class FinancingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Financing
        fields = ['id', 'jsonfield']