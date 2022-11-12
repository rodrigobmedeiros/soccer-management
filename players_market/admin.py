from django.contrib import admin
from .models import Team, Player

# Register your models here.
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name", 
        "country", 
        "budget",
        "user"
    )
    
    search_fields = (
        "name", 
        "user__username",
    )

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        "first_name", 
        "last_name", 
        "country",
        "age",
        "position",
        "value",
        "transfer_list",
        'transfer_value',
        'team'
    )
    
    search_fields = (
        "first_name", 
        "last_name",
        "team__name"
    )