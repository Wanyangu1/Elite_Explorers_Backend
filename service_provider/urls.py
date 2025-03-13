from django.urls import path
from . import views

urlpatterns = [
    path("categories/", views.list_categories, name="list_categories"),
    path("providers/", views.list_providers, name="list_providers"),
    path("services/", views.list_services, name="list_services"),
    path("services/<int:service_id>/", views.service_detail, name="service_detail"),
]
