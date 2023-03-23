from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404, render


# Create your views here.
def leagues(request):
    league_list = Competition.objects.order_by('name')[:5]
    context = {'league_list': league_list}
    return render(request, 'league/leagues.html', context)

def infoLeague(request, league_id):
    league = get_object_or_404(Competition, pk=league_id)
    matches_of_league = Match.objects.filter(league_id = league_id)
    return render(request, 'league/infoLeague.html', {
        'league': league,
        'matches': matches_of_league
    })

def infoMatch(request, match_id):
    match = get_object_or_404(Match, pk=match_id)
    return render(request, 'league/infoMatch.html', {
        'match': match
    })