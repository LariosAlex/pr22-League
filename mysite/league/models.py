from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Position(models.Model):
    name = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=200)
    def __str__(self):
        return self.abbreviation

class Player(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200)
    number = models.IntegerField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.nickname
        
class Team(models.Model):
    name = models.CharField(max_length=200)
    acronym = models.CharField(max_length=10, null=True, blank=True)
    players = models.ManyToManyField(Player)
    def __str__(self):
        return self.name

class Competition(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=10, null=True, blank=True)
    teams = models.ManyToManyField(Team)
    def __str__(self):
        return self.name

class Match(models.Model):
    local = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='local')
    visitant = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='visitant')
    date = models.DateTimeField(null=True, blank=True)
    league = models.ForeignKey(Competition, on_delete=models.CASCADE, related_name='matches')
    def __str__(self):
        return '{} vs {}'.format(self.local, self.visitant)
    
class Event(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    class EventsInMatch(models.TextChoices):
        GOAL = 'G', _('Goal')
        FAULT = 'F', _('Fault')
        RED_CARD = 'RC', _('Red Card')
        YELLOW_CARD = 'YC', _('Yellow Card')

    eventType = models.CharField(
        max_length=2,
        choices = EventsInMatch.choices,
        default = EventsInMatch.GOAL,
    )

