from rest_framework import serializers

from .models import Client
from apps.invoice.models import Invoice

class ClientInvoiceSerializer(serializers.ModelSerializer):
    """Client Invoice"""
    class Meta:
        """class meta"""
        model = Invoice
        fields = (
            "id",
            "invoice_number",
            "is_sent",
            "is_paid",
            "gross_amount",
            "vat_amount",
            "net_amount",
            "get_due_date_formatted",
            "invoice_type",
            "is_credited"
        )

class ClientSerializer(serializers.ModelSerializer):
    """Client Serializers"""
    invoices = ClientInvoiceSerializer(many=True)
    class Meta:
        """Class Meta"""
        model = Client
        read_only_fields = (
            "created_at",
            "created_by"
        )
        fields = (
            "id",
            "name",
            "email",
            "id_number",
            "address1",
            "address2",
            "zipcode",
            "place",
            "country",
            "contact_person",
            "contact_reference",
            "invoices",
        )