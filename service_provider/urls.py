from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import ServiceImageViewSet, CreateServiceProviderView

router = DefaultRouter()
router.register(r"service-images", ServiceImageViewSet)

urlpatterns = [
    path("categories/", views.list_categories, name="list_categories"),
    path("providers/", views.list_providers, name="list_providers"),
    path("services/", views.list_services, name="list_services"),
    path("services/<int:service_id>/", views.service_detail, name="service_detail"),
    path("images/", include(router.urls)),
    path("providers/create/", CreateServiceProviderView.as_view(), name="create_provider")

]
