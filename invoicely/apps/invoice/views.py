from rest_framework import viewsets

from django.core.exceptions import PermissionDenied

from .serializers import InvoiceSerializer, ItemSerializer
from .models import Invoice, Item


class InvoiceViewSet(viewsets.ModelViewSet):
    """Invoice ViewSet"""
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        team = self.request.user.teams.first()
        invoice_number = team.first_invoice_number
        team.first_invoice_number = invoice_number + 1
        team.save()

        serializer.save(
            created_by=self.request.user,
            team=team,
            modified_by=self.request.user,
            invoice_number=invoice_number)

    def perform_update(self, serializer):
        obj = self.get_object()

        if self.request.user != obj.created_by:
            raise PermissionDenied("Wrong object owner")

        serializer.save()

class ItemViewSet(viewsets.ModelViewSet):
    """Item ViewSet"""
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

    def get_queryset(self):
        invoice_id = self.request.GET.get('invoice_id', 0)

        return self.queryset.filter(invoice_id=invoice_id)
