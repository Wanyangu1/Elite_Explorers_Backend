from django.contrib import admin
from django.utils.html import format_html
from .models import ServiceCategory, ServiceProvider, ServiceListing, ServiceImage


class ServiceImageInline(admin.TabularInline):
    """Allows uploading multiple images in the admin panel under a Service Listing."""
    model = ServiceImage
    extra = 1  # Allows adding extra images


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    """Admin interface for managing service categories."""
    list_display = ("name", "description", "total_services")  # Show total services in each category
    search_fields = ("name",)
    ordering = ("name",)

    def total_services(self, obj):
        """Counts how many services belong to this category."""
        return obj.servicelisting_set.count()
    total_services.short_description = "Total Services"


@admin.register(ServiceProvider)
class ServiceProviderAdmin(admin.ModelAdmin):
    """Admin interface for managing service providers."""
    list_display = ("business_name", "email", "phone", "verified_status", "total_listings")
    search_fields = ("business_name", "email")
    list_filter = ("verified",)
    ordering = ("business_name",)
    actions = ["approve_providers"]

    def total_listings(self, obj):
        """Counts the number of listings under a provider."""
        return obj.listings.count()
    total_listings.short_description = "Total Listings"

    def verified_status(self, obj):
        """Returns a colored label for verified status."""
        if obj.verified:
            return format_html('<span style="color:green;">✔ Verified</span>')
        return format_html('<span style="color:red;">✘ Not Verified</span>')
    verified_status.short_description = "Status"

    def approve_providers(self, request, queryset):
        """Action to bulk-approve service providers."""
        queryset.update(verified=True)
        self.message_user(request, "Selected providers have been approved.")
    approve_providers.short_description = "Approve Selected Providers"


@admin.register(ServiceListing)
class ServiceListingAdmin(admin.ModelAdmin):
    """Admin interface for managing service listings."""
    list_display = ("title", "provider", "category", "price", "available", "created_at", "thumbnail")
    search_fields = ("title", "provider__business_name", "category__name")
    list_filter = ("available", "category")
    ordering = ("-created_at",)
    inlines = [ServiceImageInline]  # Allows adding multiple images directly
    actions = ["mark_as_available", "mark_as_unavailable"]

    def thumbnail(self, obj):
        """Displays the first image of the service listing in the admin panel."""
        first_image = obj.images.first()
        if first_image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 5px;" />', first_image.image.url)
        return "(No Image)"
    thumbnail.short_description = "Preview"

    def mark_as_available(self, request, queryset):
        """Action to mark selected services as available."""
        queryset.update(available=True)
        self.message_user(request, "Selected services are now available.")
    mark_as_available.short_description = "Mark as Available"

    def mark_as_unavailable(self, request, queryset):
        """Action to mark selected services as unavailable."""
        queryset.update(available=False)
        self.message_user(request, "Selected services are now unavailable.")
    mark_as_unavailable.short_description = "Mark as Unavailable"


@admin.register(ServiceImage)
class ServiceImageAdmin(admin.ModelAdmin):
    """Admin interface for managing service images."""
    list_display = ("service", "image_preview")
    search_fields = ("service__title",)
    
    def image_preview(self, obj):
        """Displays a small preview of images in the admin panel."""
        return format_html('<img src="{}" width="50" height="50" style="border-radius: 5px;" />', obj.image.url)
    image_preview.short_description = "Preview"
