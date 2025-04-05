from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceSubmissionViewSet

# Initialize the router
router = DefaultRouter()
router.register(r'PropertyToList', ServiceSubmissionViewSet)

urlpatterns = [
    path('submit/', include(router.urls)),  # API endpoint for service submissions
]
