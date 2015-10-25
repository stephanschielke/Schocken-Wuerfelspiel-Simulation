# coding=utf-8

from Wurf import Wurf

class Zug(object):

    def __init__(self, spieler):
        self.spieler = spieler
        self.wuerfe = []
        self.endergebnis = None

    def __str__(self):
        return "{0} mit Endergebnis {1}".format(self.spieler, self.endergebnis)

    def getLastWurf(self):
        return self.wuerfe[len(self.wuerfe)-1]

    def addWurf(self, wurf):
        self.wuerfe.append(wurf)

    def aktuellerWurf(self):
        return len(self.wuerfe)+1

    def setEndergebnis(self, endergebnis):
        self.endergebnis = endergebnis

    def getEndergebnis(self):
        return self.endergebnis

    def getSpieler(self):
        return self.spieler

    def __lt__(self, other):
        return self.getEndergebnis() < other.getEndergebnis()

    def __le__(self, other):
        return self.getEndergebnis() <= other.getEndergebnis()

    def __eq__(self, other):
        if other == None :
            return False

        return self.getEndergebnis() == other.getEndergebnis()

    def __ne__(self, other):
        if other == None :
            return True

        return self.getEndergebnis() != other.getEndergebnis()

    def __gt__(self, other):
        return self.getEndergebnis() > other.getEndergebnis()

    def __ge__(self, other):
        return self.getEndergebnis() >= other.getEndergebnis()