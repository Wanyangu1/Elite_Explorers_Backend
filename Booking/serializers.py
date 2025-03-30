from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    service_title = serializers.CharField(allow_blank=False, allow_null=False)
    class Meta:
        model = Booking
        exclude = ['user']  # ✅ This prevents the API from requiring a user

