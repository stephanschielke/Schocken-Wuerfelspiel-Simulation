# coding=utf-8

class Spiel(object):

    def __init__(self, nummer):
        self.nummer = nummer
        self.haelften = []

    def __str__(self):
        return "Spiel Nr. {0}".format(self.nummer)

    def addHaelfte(self, haelfte):
        self.haelften.append(haelfte)

    def isEnde(self):
        if len(self.haelften) == 3 :
            return True
        elif len(self.haelften) == 2 :
            """ Beide Hälften müssen vom gleichen Spieler verloren worden sein """
            return self.haelften[0].verlierer == self.haelften[1].verlierer
        else :
            return False

    def getAktuelleHaelfteNummer(self):
        return len(self.haelften)

    def getVerlierer(self):
        if self.isEnde() :
            return self.haelften[len(self.haelften)-1].verlierer
        else :
            return False