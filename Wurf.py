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

    def getSpielerWuerfel(self):
        return spieler.getSpielerwuerfel()

    def getErgebnis(self):
        self.ergebnis = Ergebnis([w.getAugenzahl() for w in spieler.getSpielerwuerfel()])
        return self.ergebnis

    def set_Ergebnis(self, ergebnis):
        self.ergebnis = ergebnis

        #if ergebnis.isEndergebnis:
            #self.ergebnis.save()