from django.db import models
from django.conf import settings

class ServiceCategory(models.Model):
    """Defines categories such as Hotels, Rentals, Tours, etc."""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class ServiceProvider(models.Model):
    """Stores information about businesses or individuals providing services."""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=255)
    description = models.TextField()
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255, blank=True)
    website = models.URLField(blank=True, null=True)
    verified = models.BooleanField(default=False)  # Admin approval required

    def __str__(self):
        return self.business_name


class ServiceListing(models.Model):
    """Stores details of each service offered by a provider."""
    provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE, related_name="listings")
    category = models.ForeignKey(ServiceCategory, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ServiceImage(models.Model):
    """Allows storing multiple images for a single service listing."""
    service = models.ForeignKey(ServiceListing, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="service_images/")

    def __str__(self):
        return f"Image for {self.service.title}"
