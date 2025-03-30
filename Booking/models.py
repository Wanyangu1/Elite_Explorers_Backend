from django.db import models
from django.conf import settings

class Booking(models.Model):
    service_title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.TextField()
    provider = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Customer Details
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20)
    persons = models.IntegerField()
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    special_request = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.service_title} by {self.customer_name}"
