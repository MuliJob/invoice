"""Client Views"""
# from django.shortcuts import render

from rest_framework import viewsets

from .serializers import ClientSerializer
from .models import Client

class ClientViewSet(viewsets.ModelViewSet):
    """View for clients"""
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

    def get_queryset(self):
        """Overwriting the queryset"""
        return self.queryset.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        """Getting user created_by"""
        serializer.save(created_by=self.request.user)
