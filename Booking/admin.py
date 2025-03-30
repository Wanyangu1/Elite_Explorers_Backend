from django.contrib import admin
from django.utils.html import format_html
from import_export.admin import ExportMixin
from .models import Booking

class BookingAdmin(ExportMixin, admin.ModelAdmin):
    list_display = (
        "id",
        "service_title",
        "customer_name",
        "customer_email",
        "persons",
        "check_in_date",
        "check_out_date",
        "price",
        "status_display",
        "created_at",
    )
    list_filter = ("category", "provider", "created_at", "check_in_date")
    search_fields = ("service_title", "customer_name", "customer_email", "provider")
    date_hierarchy = "created_at"
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)
    
    fieldsets = (
        ("Service Details", {
            "fields": ("service_title", "category", "description", "provider", "location", "price")
        }),
        ("Customer Details", {
            "fields": ("customer_name", "customer_email", "customer_phone", "persons")
        }),
        ("Booking Information", {
            "fields": ("check_in_date", "check_out_date", "special_request", "created_at")
        }),
    )

    def status_display(self, obj):
        """
        Display booking status with colored indicators.
        """
        if obj.check_in_date and obj.check_out_date:
            return format_html('<span style="color: green; font-weight: bold;">Confirmed</span>')
        return format_html('<span style="color: red; font-weight: bold;">Pending</span>')

    status_display.short_description = "Status"

    actions = ["mark_as_confirmed", "mark_as_pending", "export_selected"]

    def mark_as_confirmed(self, request, queryset):
        """
        Mark selected bookings as confirmed.
        """
        queryset.update(check_in_date="2024-12-01")  # Example: You can set a default date
        self.message_user(request, "Selected bookings have been marked as confirmed.")

    mark_as_confirmed.short_description = "Mark as Confirmed"

    def mark_as_pending(self, request, queryset):
        """
        Mark selected bookings as pending.
        """
        queryset.update(check_in_date=None, check_out_date=None)
        self.message_user(request, "Selected bookings are now pending.")

    mark_as_pending.short_description = "Mark as Pending"

admin.site.register(Booking, BookingAdmin)
