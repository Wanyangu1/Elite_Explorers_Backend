from rest_framework import serializers
from .models import ServiceCategory, ServiceProvider, ServiceListing, ServiceImage
from rest_framework import serializers


class ServiceCategorySerializer(serializers.ModelSerializer):
    """Serializer for service categories."""
    
    class Meta:
        model = ServiceCategory
        fields = ["id", "name", "description"]


class ServiceProviderSerializer(serializers.ModelSerializer):
    """Serializer for service providers."""

    class Meta:
        model = ServiceProvider
        fields = ["id", "user", "business_name", "description", "phone", "email", "address", "website", "verified"]
        read_only_fields = ["verified"]  # Service providers cannot verify themselves

class ServiceImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = ServiceImage
        fields = ["id", "service", "image_url"]

    def get_image_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image.url) if obj.image else None



class ServiceListingSerializer(serializers.ModelSerializer):
    """Serializer for service listings, including multiple images."""
    
    provider = ServiceProviderSerializer(read_only=True)  # Nested provider details
    category = serializers.SlugRelatedField(slug_field="name", queryset=ServiceCategory.objects.all())
    images = ServiceImageSerializer(many=True, read_only=True)  # Nested images
    
    class Meta:
        model = ServiceListing
        fields = ["id", "provider", "category", "title", "description", "price", "available", "location", "created_at", "images"]
        read_only_fields = ["created_at"]
