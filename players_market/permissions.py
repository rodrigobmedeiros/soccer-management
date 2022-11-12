from rest_framework import permissions
from .models import Team, Player

class IsTeamOwner(permissions.BasePermission):
    """
    Custom permission to only allow team owners operate over it and its players.
    """

    def has_object_permission(self, request, view, obj):
        """
        Method to define that only owners can operate over certain object
        """

        # To make this validation correct, it's needed to verify the object instance
        # Giving different treatments depending of the type.
        if isinstance(obj, Team):

            return obj.user == request.user

        elif isinstance(obj, Player):

            return obj.team.user == request.user