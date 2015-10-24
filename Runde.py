# coding=utf-8

from Wurf import Wurf

class Runde(object):

    def __init__(self):
        self.zuege = []
        self.verlierer = None

    def setVerlierer(self, spieler):
        self.verlierer = spieler

    def addZug(self, zug):
        self.zuege.append(zug)

    def getWinningWurf(self):
        """ TODO """
        return self.zuege[len(self.zuege)].getLastWurf()

    def getAktuelleZugNummer(self):
        return len(self.zuege)