from django.urls import path

from . import views, api

app_name = 'league'
urlpatterns = [
    path('', views.leagues, name='leagues'),
    path('<int:league_id>/info', views.infoLeague, name='league'),
    path('<int:league_id>/matches/', views.leagueMatches, name='matches'),
    path('<int:match_id>/', views.infoMatch, name='match'),
    path('<int:league_id>/clasification/', views.clasification, name='clasification'),
    path('menu/', views.menu, name='menu'),
    path('createLeague/', views.createLeague, name='addLeague'),
    path('createTeam/', views.createTeam, name='addTeam'),
    path('match/', views.createMatch, name='createMatch'),



    path('api/get_leagues', api.getLeagues, name='getLeagues'),
    path('api/get_teams/<int:league_id>', api.getTeams, name='getTeams')
]