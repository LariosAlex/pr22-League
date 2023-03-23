from django.contrib import admin
from .models import *
class PlayerAdmin(admin.ModelAdmin):
    exclude = ()

class MatchAdmin(admin.ModelAdmin):
    exclude = ()

admin.site.register(Player, PlayerAdmin)
admin.site.register(Team)
admin.site.register(Competition)
admin.site.register(Position)
admin.site.register(Match)
admin.site.register(Event)