from rest_framework import viewsets
from .models import ServiceSubmission
from .serializers import ServiceSubmissionSerializer

class ServiceSubmissionViewSet(viewsets.ModelViewSet):
    queryset = ServiceSubmission.objects.all()
    serializer_class = ServiceSubmissionSerializer

    # If you need custom behavior for image uploads, override the perform_create and perform_update methods
    def perform_create(self, serializer):
        # Custom logic for handling image uploads or other related fields
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        # Handle update logic for service submission and images
        serializer.save()
