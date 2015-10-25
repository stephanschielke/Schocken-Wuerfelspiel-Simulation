# coding=utf-8

class Haelfte(object):

    MAX_STRAFSTEINE = 13

    def __init__(self):
        self.strafsteine = Haelfte.MAX_STRAFSTEINE
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
