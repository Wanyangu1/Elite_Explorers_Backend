# flights/admin.py

from django.contrib import admin
from .models import FlightSearch

@admin.register(FlightSearch)
class FlightSearchAdmin(admin.ModelAdmin):
    list_display = ('origin', 'destination', 'depart_date', 'created_at')
    search_fields = ('origin', 'destination')
