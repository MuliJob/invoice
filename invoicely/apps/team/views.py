from rest_framework import viewsets
from django.core.exceptions import PermissionDenied
from .models import Team
from .serializers import TeamSerializer

class TeamViewSet(viewsets.ModelViewSet):
    """Team Class Viewset"""
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

    def get_queryset(self):
        teams = self.request.user.teams.all()

        if not teams:
            Team.objects.create(name='', id_number='', created_by=self.request.user)

        return self.queryset.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        obj = self.get_object()

        if self.request.user != obj.created_by:
            raise PermissionDenied("Wrong object owner")

        serializer.save()
