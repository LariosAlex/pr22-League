from django.urls import path

from . import views

app_name = 'league'
urlpatterns = [
    path('', views.leagues, name='leagues'),
    path('<int:league_id>/', views.infoLeague, name='league'),
    path('matches/<int:league_id>/', views.leagueMatches, name='matches'),
    path('match/<int:match_id>', views.infoMatch, name='match'),
    path('clasification/<int:league_id>', views.clasification, name='clasification')
]