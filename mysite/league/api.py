from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django import forms
from django.shortcuts import redirect
from django.http import JsonResponse

def getLeagues(request):
    leagues = list( Competition.objects.all().values() )
    return JsonResponse({
            "status": "OK",
            "leagues": leagues,
        }, safe=False)

def getTeams(request, league_id):
    league = (Competition.objects.get(pk = league_id))
    teams = list(league.teams.values())
    return JsonResponse({
            "status": "OK",
            "teams": teams,
        }, safe=False)