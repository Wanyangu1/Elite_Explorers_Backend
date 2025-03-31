from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())  # Automatically set the logged-in user

    class Meta:
        model = Booking
        fields = '__all__'  # Include all fields
