from rest_framework import serializers

from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    """Client Serializers"""
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
        )