# coding=utf-8

from Spieler import Spieler
from Becher import Becher
from Wuerfel import Wuerfel
from Ergebnis import Ergebnis


class Wurf(object):
    def __init__(self, nummer, spieler):
        self.nummer = nummer
        self.spieler = spieler
        self.ergebnis = None

    def __str__(self):
        return "{0}. Wurf"

    def get_spielerwuerfel(self):
        return self.spieler.getSpielerwuerfel()

    def get_ergebnis(self):
        self.ergebnis = Ergebnis([w.getAugenzahl() for w in self.spieler.getSpielerwuerfel()])
        return self.ergebnis

    def set_ergebnis(self, ergebnis):
        self.ergebnis = ergebnis

        # if ergebnis.isEndergebnis:
        # self.ergebnis.save
