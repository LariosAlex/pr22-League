from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django import forms
from django.shortcuts import redirect

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

def leagueMatches(request, league_id):
    league = get_object_or_404(Competition, pk=league_id)
    return render(request, 'league/matches.html', {
        'league': league
    })

def clasification(request, league_id):
    league = get_object_or_404(Competition, pk=league_id)
    matches = Match.objects.filter(league_id = league_id)
    teams = [team for team in league.teams.all()]
    dict_teams = {}
    for team in teams:
        dict_teams[team.name] = 0
    
    teams_puntuation = []

    for match in matches:
        goal_local = match.event_set.filter(eventType=Event.EventsInMatch.GOAL, team=match.local).count()
        goal_visitant = match.event_set.filter(eventType=Event.EventsInMatch.GOAL, team=match.visitant).count()
        if(goal_local > goal_visitant):
            dict_teams[match.local.name] = dict_teams[match.local.name] + 3
        elif(goal_local < goal_visitant):
            dict_teams[match.visitant.name] = dict_teams[match.visitant.name] + 3
        else:
            dict_teams[match.local.name] = dict_teams[match.local.name] + 1
            dict_teams[match.visitant.name] = dict_teams[match.visitant.name] + 1

    for team, points in dict_teams.items():
        teams_puntuation.append([team, points])

    clasification_order = sorted(teams_puntuation, key=lambda team: team[1], reverse=True)

    return render(request, 'league/clasification.html', {
        'league': league,
        'teams': clasification_order,
    })

class MenuForm(forms.Form):
    lliga = forms.ModelChoiceField(queryset=Competition.objects.all())
 
def menu(request):
    form = MenuForm()
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            lliga = form.cleaned_data.get("lliga")
            return redirect('league:clasification',lliga.id)
    return render(request, "league/menu.html",{
                    "form": form,
            })

class MenuForm(forms.Form):
    lliga = forms.ModelChoiceField(queryset=Competition.objects.all())
 
def menu(request):
    form = MenuForm()
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            lliga = form.cleaned_data.get("lliga")
            return redirect('league:clasification',lliga.id)
    return render(request, "league/menu.html",{
                    "form": form,
            })

class LeagueForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = ['name', 'country', 'teams']

def createLeague(request):
    form = LeagueForm()
    message = ''

    if request.method == 'POST':
        form = LeagueForm(request.POST)
        if form.is_valid:
            leagueName = form.cleaned_data.get('name')
            if Competition.objects.filter(name = leagueName):
                message = 'El nom de la lliga ja existeix'
            else:
                message = 'La lliga ha sigut creada correctament'
                form.save();

    return render(request, "league/addLeague.html",{
        "form": form,
        "message" : message
    })

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'players']

def createTeam(request):
    form = TeamForm()
    message = ''

    if request.method == 'POST':
        form = LeagueForm(request.POST)
        if form.is_valid:
            teamName = form.cleaned_data.get('name')
            if Competition.objects.filter(name = teamName):
                message = 'El nom del equip ja existeix'
            else:
                message = 'El equip ha sigut creat correctament'
                form.save();

    return render(request, "league/addTeam.html",{
        "form": form,
        "message" : message
    })

def createMatch(request):
    return render(request,'league/createMatch.html')
