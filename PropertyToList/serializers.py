from rest_framework import serializers
from .models import ServiceSubmission, ServiceImageNew

class ServiceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceImageNew
        fields = ['id', 'image', 'uploaded_at']

class ServiceSubmissionSerializer(serializers.ModelSerializer):
    # Nested serializer for service images
    service_images = ServiceImageSerializer(many=True, required=False)
    
    class Meta:
        model = ServiceSubmission
        fields = [
            'id', 'user', 'business_name', 'provider_description', 'phone', 'email', 'address', 'website',
            'category', 'service_title', 'service_description', 'price', 'availability', 'location', 
            'submitted_at', 'service_images'
        ]
