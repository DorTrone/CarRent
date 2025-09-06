from rest_framework import viewsets
from .models import Rents
from .serializers import RentSerializer

class RentViewSet(viewsets.ModelViewSet):
    queryset = Rents.objects.all()
    serializer_class = RentSerializer

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()
    
    def perform_destroy(self, instance):
        instance.delete()
    
    def perform_partial_update(self, serializer):
        serializer.save()
    