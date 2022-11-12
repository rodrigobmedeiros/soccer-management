from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from players_market.models import Team, Player
import pytest
import json

# Create your tests here.

@pytest.fixture
def client(request):
    return APIClient()

@pytest.fixture 
def user_1(request):
    body = {
        "username": "RodrigoB",
        "password": "123456ABCabc",
        "password2": "123456ABCabc",
        "email": "rodrimedeiros@email.com",
        "first_name": "rodrigo",
        "last_name": "bernardo medeiros"
    }

    return body

@pytest.fixture 
def user_2(request):
    body = {
        "username": "SecondTeam",
        "password": "123456ABCabc",
        "password2": "123456ABCabc",
        "email": "secondteam@email.com",
        "first_name": "rodrigo",
        "last_name": "bernardo medeiros"
    }

    return body

@pytest.mark.django_db
def test_get_team(client: APIClient, user_1: dict):

    client.post(path='/auth/register/', data=json.dumps(user_1), content_type='application/json')
    client.login(username=user_1['username'], password=user_1['password'])
    response = client.get(path='/team/')

    team_data = response.data

    assert response.status_code == 200
    assert team_data["user"] == "RodrigoB"
    assert team_data["name"] == "team_RodrigoB"
    assert team_data["country"] == "United States"
    assert team_data["team_value"] == 20000000
    assert team_data["budget"] == 5000000

@pytest.mark.django_db
def test_get_players(client: APIClient, user_1: dict):

    client.post(path='/auth/register/', data=json.dumps(user_1), content_type='application/json')
    client.login(username=user_1['username'], password=user_1['password'])
    response = client.get(path='/players/')

    first_player = response.data[0]

    assert first_player["first_name"] == "first name_1"
    assert first_player["last_name"] == "last name_1"
    assert first_player["country"] == "United States"
    assert first_player["age"] >= 18 and first_player["age"] <= 40
    assert first_player["value"] == 1000000
    assert first_player["team"] == "team_RodrigoB"

@pytest.mark.django_db
def test_get_player_by_id(client: APIClient, user_1: dict):
    client.post(path='/auth/register/', data=json.dumps(user_1), content_type='application/json')
    client.login(username=user_1['username'], password=user_1['password'])

    first_player = client.get(path=f'/players/1/')

    assert first_player.data["first_name"] == "first name_1"
    assert first_player.data["last_name"] == "last name_1"
    assert first_player.data["country"] == "United States"
    assert first_player.data["id"] == 1
    assert (first_player.data["age"] >= 18) and (first_player.data["age"] <= 40)
    assert first_player.data["team"] == "team_RodrigoB"

@pytest.mark.django_db
def test_edit_player_by_id(client: APIClient, user_1: dict):

    client.post(path='/auth/register/', data=json.dumps(user_1), content_type='application/json')
    client.login(username=user_1['username'], password=user_1['password'])

    new_player_info = {
        'first_name': 'Neymar',
        'last_name': 'Junior',
        'country': 'Brazil'
    }

    client.put(path='/players/1/', data=json.dumps(new_player_info), content_type='application/json')

    player_updated_from_database: Player = Player.objects.get(id=1)

    assert player_updated_from_database.first_name == new_player_info['first_name']
    assert player_updated_from_database.last_name == new_player_info['last_name']
    assert player_updated_from_database.country == new_player_info['country']

@pytest.mark.django_db
def test_edit_team_by_id(client: APIClient, user_1: dict):

    client.post(path='/auth/register/', data=json.dumps(user_1), content_type='application/json')
    client.login(username=user_1['username'], password=user_1['password'])

    new_team_info = {
        'name': 'Manchester City',
        'country': 'England',
    }

    client.put(path='/team/1/', data=json.dumps(new_team_info), content_type='application/json')

    team_updated_from_database: Team = Team.objects.get(id=1)

    assert team_updated_from_database.name == new_team_info['name']
    assert team_updated_from_database.country == new_team_info['country']

@pytest.mark.django_db
def test_add_player_to_transfer_market_list(client: APIClient, user_1: dict):

    client.post(path='/auth/register/', data=json.dumps(user_1), content_type='application/json')
    client.login(username=user_1['username'], password=user_1['password'])

    add_player_to_transfer_market_list_info = {
        'transfer_list':  True,
        'transfer_value': 1500000
    }

    client.put(
        path='/transfer-market/1/add/', 
        data=json.dumps(add_player_to_transfer_market_list_info), 
        content_type='application/json'
    )

    player_added_from_database: Player = Player.objects.get(id=1)

    assert player_added_from_database.transfer_list
    assert player_added_from_database.transfer_value == add_player_to_transfer_market_list_info['transfer_value']

@pytest.mark.django_db
def test_buy_player_from_transfer_market_list(client: APIClient, user_1: dict, user_2: dict):

    # Register two users
    client.post(path='/auth/register/', data=json.dumps(user_1), content_type='application/json')
    client.post(path='/auth/register/', data=json.dumps(user_2), content_type='application/json')

    # add one player from user 1 to transfer market list
    client.login(username=user_1['username'], password=user_1['password'])
    player_original: Player = Player.objects.get(id=1)
    player_original.transfer_list = True
    player_original.transfer_value = 1500000
    player_original.save() 

    # buy player from transfer market list usinsg user 2
    client.login(username=user_2['username'], password=user_2['password'])
    client.put(path='/transfer-market/1/buy/', data={}, content_type='application/json')

    # get player from database to verify all operations
    player_updated: Player = Player.objects.get(id=1)

    # get users
    user_1: User = User.objects.get(username=user_1['username'])
    user_2: User = User.objects.get(username=user_2['username'])

    # get teams
    team_1: Team = Team.objects.get(user=user_1)
    team_2: Team = Team.objects.get(user=user_2)

    assert player_updated.value >= 1100000 and player_updated.value <= 2000000
    assert player_updated.team == team_2
    assert not player_updated.transfer_list
    
    assert team_1.team_value == 19000000
    assert team_1.budget == 6500000
    assert team_2.team_value == 20000000 + player_updated.value
    assert team_2.budget == 3500000

@pytest.mark.django_db
def test_get_transfer_market_list(client: APIClient, user_1: dict):

    client.post(path='/auth/register/', data=json.dumps(user_1), content_type='application/json')
    client.login(username=user_1['username'], password=user_1['password'])

    player: Player = Player.objects.get(id=1)
    player.transfer_list = True 
    player.transfer_value = 1500000
    player.save()

    response = client.get(path='/transfer-market/')

    assert len(response.data) == 1

