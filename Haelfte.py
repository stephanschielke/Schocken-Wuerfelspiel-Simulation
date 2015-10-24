# coding=utf-8

class Haelfte(object):

    def __init__(self):
        self.runden = []
        self.verlierer = None

    def addRunde(self, runde):
        self.runden.append(runde)

    def setVerlierer(self, spieler):
        self.verlierer = spieler

    def getVerlierer(self):
        return self.verlierer

    def getAktuelleRundenNummer(self):
        return len(self.runden)