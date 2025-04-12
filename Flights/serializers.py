# flights/serializers.py

from rest_framework import serializers
from .models import FlightSearch

class FlightSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightSearch
        fields = ['id', 'origin', 'destination', 'depart_date', 'return_date']
