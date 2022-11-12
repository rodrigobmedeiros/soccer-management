from django.contrib.auth.models import User
from .models import Team, Player
import random

def create_initial_team(user: User):
    """
    Function called during a new user registration proccess, responsible for create new team for him.
    """

    # creation of a new team. To start, it follows some initial considerations:
    # 1. team name will be the word team plus username
    # 2. country will be set as United States as default
    # All these fields can be changed later.
    # Team budget is not setted because all teams start with default value of $5.000.000
    team = Team(
        name = 'team_' + user.username,
        country='United States',
        user=user
    )
    team.save()

    # Creation of Players
    # 3 goalkeepers
    # 6 defenders
    # 6 midfielders
    # 5 attackers

    team_initial_config = [
        ('goalkeeper', 3),
        ('defender' , 6),
        ('midfielder', 6),
        ('attacker', 5)
    ]

    player_counter = 1

    for players_info in team_initial_config:

        player_position = players_info[0]
        number_of_players = players_info[1]

        

        for _ in range(number_of_players):

            # Some fields are not defined here because default values:
            # 1. value: All players start with value of $1.000.000
            # 2. transfer_lis: All players start out of transer_list
            # 3. transfer_value: Default value is the same of value
            player = Player(
                first_name='first name_' + str(player_counter), 
                last_name='last name_' + str(player_counter),
                country='United States',
                age=random.randint(18, 40),
                position=player_position,
                team=team
            )

            player.save()
            player_counter += 1


def finalize_player_sale(player: Player, team_buyer: Team, team_seller: Team):
    """
    Function called to finalize player sale, updating player value, budget and team 
    value for each team.
    """
    # 1º: Update player team
    player.team = team_buyer

    # 2º: Update player value considering a random factor between 10% and 100%
    random_factor = random.randint(10, 100) + 100
    player.value *= (round(random_factor / 100, 2))

    # 3º: Update transfer_list flag in order to remove bought player from Transfer Market
    player.transfer_list = False

    # Persist instance(player) modifications to database
    player.save()

    # Update budget for both teams involved in the operation
    team_buyer.budget -= player.transfer_value
    team_seller.budget += player.transfer_value
    
    # Update team value after operation
    team_buyer.update_team_value()
    team_seller.update_team_value()

    # Persist team modifications to database
    team_seller.save()
    team_buyer.save()