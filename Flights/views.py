# flights/views.py

import requests
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import FlightSearch
from .serializers import FlightSearchSerializer

class FlightSearchAPIView(APIView):
    def post(self, request):
        serializer = FlightSearchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.validated_data

            token = settings.TRAVELPAYOUTS_TOKEN
            url = "https://api.travelpayouts.com/v2/prices/latest"

            params = {
                'origin': data['origin'],
                'destination': data['destination'],
                'depart_date': data['depart_date'],
                'return_date': data['return_date'] or '',
                'currency': 'usd',
                'page': 1,
                'limit': 10,
                'token': token
            }

            response = requests.get(url, params=params)
            if response.status_code == 200:
                return Response(response.json(), status=status.HTTP_200_OK)
            else:
                return Response(
                    {"error": "Failed to fetch flights."},
                    status=response.status_code
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# NOT RECOMMENDED unless you sanitize query params heavily

class FlightSearchAPIView(APIView):
    def get(self, request):
        origin = request.GET.get('origin')
        destination = request.GET.get('destination')
        depart_date = request.GET.get('depart_date')
        return_date = request.GET.get('return_date', '')

        token = settings.TRAVELPAYOUTS_TOKEN
        url = "https://api.travelpayouts.com/v2/prices/latest"

        params = {
            'origin': origin,
            'destination': destination,
            'depart_date': depart_date,
            'return_date': return_date,
            'currency': 'usd',
            'limit': 10,
            'token': token
        }

        response = requests.get(url, params=params)
        return Response(response.json(), status=response.status_code)
