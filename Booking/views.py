from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Booking
from .serializers import BookingSerializer

@api_view(['POST'])
def create_booking(request):
    """
    Handles booking creation.
    """
    try:
        data = request.data
        booking_data = {
            "service_title": data.get("title"),
            "category": data.get("category"),
            "description": data.get("description"),
            "provider": data.get("provider"),
            "location": data.get("location"),
            "price": data.get("price"),
            "customer_name": data["customer"]["name"],
            "customer_email": data["customer"]["email"],
            "customer_phone": data["customer"]["phone"],
            "persons": data["customer"]["persons"],
            "check_in_date": data["customer"]["check_in_date"],
            "check_out_date": data["customer"]["check_out_date"],
            "special_request": data["customer"].get("notes", ""),
        }

        serializer = BookingSerializer(data=booking_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Booking confirmed!", "data": serializer.data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
