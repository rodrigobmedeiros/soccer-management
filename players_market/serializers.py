from rest_framework import serializers 
from .models import Team, Player
from .utils import finalize_player_sale
import random

class TeamSerializer(serializers.ModelSerializer):
    """
    General class used to serialize Team model with all main information.
    """
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Team 
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'budget': {'read_only': True},
            'team_value': {'read_only': True}
        }

class PlayerSerializer(serializers.ModelSerializer):
    """
    General class used to serialize Player model with all main information.
    """
    team = serializers.ReadOnlyField(source='team.name')

    class Meta:
        model = Player 
        fields = [
            'id',
            'first_name',
            'last_name',
            'country',
            'age',
            'position',
            'value',
            'team'
        ]
        extra_kwargs = {
            'id': {'read_only': True},
            'age': {'read_only': True},
            'position': {'read_only': True},
            'value': {'read_only': True}
        }

class PlayerTransferMarketSerializer(serializers.ModelSerializer):
    """
    General class used to serialize Player model focusing on Transfer Market
    """
    team = serializers.ReadOnlyField(source='team.name')

    class Meta:
        model = Player 
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'age': {'read_only': True},
            'position': {'read_only': True},
            'value': {'read_only': True},
            'first_name': {'read_only': True},
            'last_name': {'read_only': True},
            'country': {'read_only': True}
        }

class PlayerBuyOperationSerializer(serializers.ModelSerializer):
    """
    Class used to serialize Player model  to be used into buy operations. 
    """
    team = serializers.ReadOnlyField(source='team.name')

    class Meta:
        model = Player
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'first_name': {'read_only': True},
            'last_name': {'read_only': True},
            'country': {'read_only': True},
            'age': {'read_only': True},
            'position': {'read_only': True},
            'value': {'read_only': True},
            'transfer_list': {'read_only': True},
            'transfer_value': {'read_only': True},
            'team': {'read_only': True},
        }


    def update(self, instance, validated_data):
        
        # Get user from the current session
        user = self.context['request'].user

        # Get both teams involved in the sales operation
        team_buyer = Team.objects.get(user=user)
        team_seller = instance.team

        if team_seller.user == user:
            raise serializers.ValidationError("Users cannot buy players from their own team")

        if instance.transfer_value > team_buyer.budget:
            raise serializers.ValidationError("Not enough money to buy a new player")

        # Finalize player sale with this function from utils.
        finalize_player_sale(instance, team_buyer, team_seller)

        return instance