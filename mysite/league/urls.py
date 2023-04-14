from django.urls import path

from . import views

app_name = 'league'
urlpatterns = [
    path('', views.leagues, name='leagues'),
    path('<int:league_id>/info', views.infoLeague, name='league'),
    path('<int:league_id>/matches/', views.leagueMatches, name='matches'),
    path('<int:match_id>/', views.infoMatch, name='match'),
    path('<int:league_id>/clasification/', views.clasification, name='clasification'),
    path('menu/', views.menu, name='menu')
]