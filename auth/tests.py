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

@pytest.mark.django_db
def test_register_new_user(client: APIClient, user_1: dict):
    
    response = client.post(path='/auth/register/', data=json.dumps(user_1), content_type='application/json')
    user = User.objects.get(email=response.data['email'])
    team = Team.objects.get(user=user)
    players = Player.objects.filter(team=team)
    goalkeepers = players.filter(position='goalkeeper')
    defenders = players.filter(position='defender')
    midfielders = players.filter(position='midfielder')
    attackers = players.filter(position='attacker')

    assert team.name == 'team_RodrigoB'
    assert len(players) == 20
    assert team.team_value == 20000000
    assert len(goalkeepers) == 3
    assert len(defenders) == 6
    assert len(midfielders) == 6
    assert len(attackers) == 5

@pytest.mark.django_db
def test_login_success(client: APIClient, user_1: User):

    client.post(path='/auth/register/', data=json.dumps(user_1), content_type='application/json')

    is_logged = client.login(username=user_1['username'], password=user_1['password'])

    assert is_logged

@pytest.mark.django_db
def test_login_failure(client: APIClient, user_1: User):

    is_logged = client.login(username='non-existent user', password='non-existent user')

    assert not is_logged
