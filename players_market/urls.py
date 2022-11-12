from django.urls import path 
from .views import (
    AddPlayerIntoMarketTransferList,
    TransferMarketViewSet,
    PlayerBuyOperation,
    PlayerViewSet,
    PlayerDetail,
    TeamViewSet, 
    TeamDetail,
)

app_name = 'players_market'

urlpatterns = [
    path('team/<int:pk>/', TeamDetail.as_view()),
    path('team/', TeamViewSet.as_view({'get': 'retrieve'})),
    path('players/', PlayerViewSet.as_view({'get': 'list'})),
    path('players/<int:pk>/', PlayerDetail.as_view()),
    path('transfer-market/', TransferMarketViewSet.as_view({'get': 'list'})),
    path('transfer-market/<int:pk>/add/', AddPlayerIntoMarketTransferList.as_view()),
    path('transfer-market/<int:pk>/buy/', PlayerBuyOperation.as_view())
]