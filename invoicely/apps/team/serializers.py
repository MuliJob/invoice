"""Team Serializer"""
from rest_framework import serializers

from .models import Team

class TeamSerializer(serializers.ModelSerializer):
    """Team Serializer"""
    class Meta:
        """Class Meta"""
        model = Team
        read_only_field = (
            "created_by"
        ),
        fields = (
            "id",
            "name",
            "id_number",
            "first_invoice_number",
            "bankaccount"
        )
