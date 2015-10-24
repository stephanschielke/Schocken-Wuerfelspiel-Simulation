# coding=utf-8

from Spieler import Spieler
from Becher import Becher
from Wuerfel import Wuerfel
from Ergebnis import Ergebnis

class Wurf(object):

    def __init__(self, nummer, spieler):
        self.nummer = nummer
        self.spieler = spieler
        self.ergebnis = Ergebnis([0,0,0])

    def __str__(self):
        return "{0}. Wurf"

    def getSpielerWuerfel(self):
        return spieler.getSpielerwuerfel()

    def getErgebnis(self):
        self.ergebnis = Ergebnis([w.getAugenzahl() for w in spieler.getSpielerwuerfel()])
        return self.ergebnis