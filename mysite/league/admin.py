from django.contrib import admin
from .models import *
class PlayerAdmin(admin.ModelAdmin):
    exclude = ()

class EventInline(admin.TabularInline):
    model = Event
    fields = ["eventType", "team", "player"]
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # filtrem els equips i només deixem els que siguin del partit
        if db_field.name == "team":
            match_id = request.resolver_match.kwargs['object_id']
            match = Match.objects.get(id=match_id)
            local = [match.local.id]
            visitant = [match.visitant.id]
            teams = local + visitant
            kwargs["queryset"] = Team.objects.filter(id__in=teams)

        if db_field.name == "player":
            match_id = request.resolver_match.kwargs['object_id']
            match = Match.objects.get(id=match_id)
            local = [player.id for player in match.local.players.all()]
            visitant = [player.id for player in match.visitant.players.all()]
            players = local + visitant
            kwargs["queryset"] = Player.objects.filter(id__in=players)

        return super().formfield_for_foreignkey(db_field, request, **kwargs) 

class MatchAdmin(admin.ModelAdmin):
    inlines = [EventInline]
    readonly_fields = ["resultat",]
    def resultat(self,obj):
        goal_local = obj.event_set.filter(eventType=Event.EventsInMatch.GOAL, team=obj.local).count()
        goal_visit = obj.event_set.filter(eventType=Event.EventsInMatch.GOAL, team=obj.visitant).count()
        return "{} - {}".format(goal_local,goal_visit)



admin.site.register(Player, PlayerAdmin)
admin.site.register(Team)
admin.site.register(Competition)
admin.site.register(Position)
admin.site.register(Match, MatchAdmin)
admin.site.register(Event)