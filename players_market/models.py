from django.db import models
from django.contrib.auth.models import User 
import random

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    team_value = models.FloatField(default=20_000_000)
    budget = models.FloatField(default=5_000_000)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)

    def update_team_value(self):
        """
        Method used to update team_value attrubute when needed.
        """
        self.team_value = Player.objects.filter(team=self).aggregate(models.Sum('value'))['value__sum']
        

    def __str__(self):
        return f'Team(name: {self.name}, country: {self.country}, user: {self.user.email})'


class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    age = models.IntegerField()
    position = models.CharField(max_length=20)
    value = models.FloatField(default=1_000_000)
    transfer_list = models.BooleanField(default=False)
    transfer_value = models.FloatField(default=1_000_000)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return f'Player(first_name: {self.first_name}, age: {self.age}, country: {self.country}, team: {self.team.name})'
