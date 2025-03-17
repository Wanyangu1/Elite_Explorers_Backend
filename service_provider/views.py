from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import ServiceCategory, ServiceProvider, ServiceListing, ServiceImage
from rest_framework import viewsets
from .serializers import ServiceImageSerializer

class ServiceImageViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint to retrieve service images."""
    queryset = ServiceImage.objects.all()
    serializer_class = ServiceImageSerializer



def list_categories(request):
    """Returns all service categories in JSON format."""
    categories = ServiceCategory.objects.all().values("id", "name", "description")
    return JsonResponse(list(categories), safe=False)


def list_providers(request):
    """Returns all service providers in JSON format."""
    providers = ServiceProvider.objects.all().values("id", "business_name", "email", "verified")
    return JsonResponse(list(providers), safe=False)


def list_services(request):
    """Returns all service listings in JSON format with multiple images."""
    services = ServiceListing.objects.all()
    data = []
    
    for service in services:
        images = list(service.images.all().values_list("image", flat=True))  # Get all images
        data.append({
            "id": service.id,
            "title": service.title,
            "description": service.description,
            "category": service.category.name if service.category else None,
            "provider": service.provider.business_name,
            "price": str(service.price),
            "available": service.available,
            "location": service.location,
            "images": images,
        })
    
    return JsonResponse(data, safe=False)


def service_detail(request, service_id):
    """Returns details of a single service listing, including multiple images."""
    service = get_object_or_404(ServiceListing, pk=service_id)
    images = list(service.images.all().values_list("image", flat=True))
    
    data = {
        "id": service.id,
        "title": service.title,
        "description": service.description,
        "category": service.category.name if service.category else None,
        "provider": service.provider.business_name,
        "price": str(service.price),
        "available": service.available,
        "location": service.location,
        "images": images,
    }
    
    return JsonResponse(data)
