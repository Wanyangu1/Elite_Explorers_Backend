from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class ServiceSubmission(models.Model):
    # Business info
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    business_name = models.CharField(max_length=255)
    provider_description = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255, blank=True)
    website = models.URLField(blank=True)

    # Service info
    category = models.CharField(max_length=100)
    service_title = models.CharField(max_length=255)
    service_description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    location = models.CharField(max_length=255)

    # Timestamp
    submitted_at = models.DateTimeField(auto_now_add=True)

    # Many-to-many relationship to the newly renamed service image model
    service_images = models.ManyToManyField('ServiceImageNew', related_name='service_submissions', blank=True)

    def __str__(self):
        return f"{self.business_name} - {self.service_title}"


class ServiceImageNew(models.Model):
    """Stores images for a service submission."""
    image = models.ImageField(upload_to='services/images/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id}"
