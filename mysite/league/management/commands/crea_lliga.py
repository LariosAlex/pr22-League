from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from faker import Faker
from datetime import timedelta
from random import randint

from league.models import *

faker = Faker(["es_CA","es_ES"])

class Command(BaseCommand):
    help = 'Crea una lliga amb equips i jugadors'

    def add_arguments(self, parser):
        parser.add_argument('titol_lliga', nargs=1, type=str)

    def handle(self, *args, **options):
        titol_lliga = options['titol_lliga'][0]
        lliga = Competition.objects.filter(name=titol_lliga)
        if lliga.count()>0:
            print("Aquesta lliga ja està creada. Posa un altre nom.")
            return

        print("Creem la nova lliga: {}".format(titol_lliga))
        lliga = Competition(name=titol_lliga)
        lliga.save()

        print("Creem equips")
        prefixos = ["RCD", "Athletic", "", "Deportivo", "Unión Deportiva", "FC"]
        for i in range(20):
            ciutat = faker.city()
            prefix = prefixos[randint(0,len(prefixos)-1)]
            if prefix:
                prefix += " "
            nom =  prefix + ciutat
            equip = Team(name=nom)
            #print(equip)
            equip.save()
            lliga.teams.add(equip)

            print("Creem jugadors de l'equip "+nom)
            for i in range(25):
                nom = faker.first_name()
                cognom1 = faker.last_name()
                jugador = Player(name=nom,last_name=cognom1,nickname=nom+" "+cognom1,number=i+1)
                #print(jugador)
                jugador.save()
                equip.players.add(jugador)

        print("Creem partits de la lliga")
        for local in lliga.teams.all():
            for visitant in lliga.teams.all():
                if local!=visitant:
                    partit = Match(local=local,visitant=visitant)
                    partit.local = local
                    partit.visitant = visitant
                    partit.league = lliga
                    partit.save()