from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response

from .models import Team, Player 
from .permissions import IsTeamOwner
from .serializers import (
    PlayerTransferMarketSerializer,
    PlayerBuyOperationSerializer,
    PlayerSerializer,
    TeamSerializer
)


# Create your views here.
class TeamDetail(generics.UpdateAPIView):
    """
    View user to update teams atributes
     - name
     - country
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsTeamOwner
    ]

class TeamViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for retrieving team info considering authenticated user.
    """

    permission_classes = [
        permissions.IsAuthenticated,
        IsTeamOwner
    ]

    def retrieve(self, request, pk=None):
        queryset = Team.objects.all()
        team = get_object_or_404(queryset, user=request.user)
        serializer = TeamSerializer(team)
        return Response(serializer.data)

class PlayerDetail(generics.RetrieveUpdateAPIView):
    """
    View user to retrieve players data and update players atributes considering a specific id.
     - first_name
     - last_name
     - country
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsTeamOwner
    ]

class PlayerViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing players info considering authenticated user.
    """

    permission_classes = [
        permissions.IsAuthenticated,
        IsTeamOwner
    ]

    def list(self, request):
        team = Team.objects.get(user=request.user)
        queryset = Player.objects.filter(team=team)
        serializer = PlayerSerializer(queryset, many=True)
        return Response(serializer.data)

class TransferMarketViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing players into transfer market list.
    """

    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def list(self, request):
        queryset = Player.objects.filter(transfer_list=True)
        serializer = PlayerTransferMarketSerializer(queryset, many=True)
        return Response(serializer.data)

class AddPlayerIntoMarketTransferList(generics.UpdateAPIView):
    """
    API view to update players including then into transfer market list.
    """
    queryset = Player.objects.all()
    serializer_class = PlayerTransferMarketSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsTeamOwner
    ]

class PlayerBuyOperation(generics.UpdateAPIView):
    """
    API view to perform buy operations of players into transfer market list.
    """
    queryset = Player.objects.filter(transfer_list=True)
    serializer_class = PlayerBuyOperationSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]