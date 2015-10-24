# coding=utf-8

from Wurf import Wurf

class Zug(object):

    def __init__(self, spieler):
        self.spieler = spieler
        self.wuerfe = []

    def getLastWurf(self):
        return self.wuerfe[len(self.wuerfe)]

    def addWurf(self, wurf):
        self.wuerfe.append(wurf)

    def aktuellerWurf(self):
        return len(self.wuerfe)+1