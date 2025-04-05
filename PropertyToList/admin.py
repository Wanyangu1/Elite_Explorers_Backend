from django.contrib import admin
from .models import ServiceSubmission, ServiceImageNew
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _


class ServiceImageInline(admin.TabularInline):
    model = ServiceSubmission.service_images.through  # Access the through table for the ManyToMany relationship
    extra = 1  # Number of empty forms to display by default in the inline
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        """Displays a preview of the image in the admin inline form."""
        return format_html('<img src="{}" width="100" height="100" />', obj.image.url)
    image_preview.short_description = _('Image Preview')


@admin.register(ServiceSubmission)
class ServiceSubmissionAdmin(admin.ModelAdmin):
    list_display = (
        'business_name',
        'service_title',
        'category',
        'email_link',
        'phone',
        'availability_status',
        'location',
        'submitted_at',
        'view_images',  # New column to display images
    )
    list_filter = (
        'category',
        'availability',
        'submitted_at',
    )
    search_fields = (
        'business_name',
        'service_title',
        'category',
        'phone',
        'email',
        'location',
    )
    readonly_fields = ('submitted_at', 'email_link', 'view_images')  # Add 'view_images' to readonly fields
    ordering = ('-submitted_at',)
    date_hierarchy = 'submitted_at'
    list_per_page = 25
    fieldsets = (
        (_('Business Information'), {
            'fields': ('user', 'business_name', 'provider_description', 'phone', 'email_link', 'address', 'website')
        }),
        (_('Service Details'), {
            'fields': ('category', 'service_title', 'service_description', 'price', 'availability', 'location')
        }),
        (_('Service Images'), {
            'fields': ('service_images',),  # Show the many-to-many field for images
            'classes': ('collapse',),
        }),
        (_('Submission Metadata'), {
            'fields': ('submitted_at',),
            'classes': ('collapse',),
        }),
    )
    inlines = [ServiceImageInline]  # Display inline form for adding images to ServiceSubmission

    def email_link(self, obj):
        if obj.email:
            return format_html(f'<a href="mailto:{obj.email}">{obj.email}</a>')
        return '-'
    email_link.short_description = 'Email'

    def availability_status(self, obj):
        if obj.availability:
            return format_html('<span style="color: green; font-weight: bold;">Available</span>')
        return format_html('<span style="color: red;">Unavailable</span>')
    availability_status.short_description = 'Availability'

    def view_images(self, obj):
        """Displays all images related to the service submission in the admin list."""
        images = obj.service_images.all()
        if images:
            return format_html(' '.join([f'<img src="{image.image.url}" width="50" height="50" />' for image in images]))
        return '-'
    view_images.short_description = _('Service Images')

    def has_add_permission(self, request):
        return True  # Or customize based on request.user

    def has_delete_permission(self, request, obj=None):
        return True  # Or customize if you want to protect some entries
