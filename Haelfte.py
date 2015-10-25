# coding=utf-8

from Config import Config
from Spieler import Spieler

class Haelfte(object):

    def __init__(self):
        self.strafsteine = Config.MAX_STRAFSTEINE
        self.runden = []
        self.verlierer = None

    def addRunde(self, runde):
        self.runden.append(runde)

    def getAktuelleRundenNummer(self):
        return len(self.runden)

    def verteileStrafsteine(self, verlierer, anzahl):
        if anzahl >= self.strafsteine :
            anzahl = self.strafsteine

        verlierer.addStrafsteine(anzahl)
        self.strafsteine -= anzahl

    def hasStrafsteine(self):
        return self.strafsteine > 0
