# coding=utf-8

from Becher import Becher
from Wuerfel import Wuerfel

class Spieler(object):

    def __init__(self, name):
        self.name = name
        self.teilnehmend = True
        self.becher = Becher(self)
        self.wuerfelList = [Wuerfel(),Wuerfel(),Wuerfel()]

    def __str__(self):
        return self.name

    def alleWuerfelInBecherLegen(self):
        print "{0} legt {1} Würfel in den Becher.".format(self, len(self.wuerfelList))
        self.becher.befuellen(self.wuerfelList)

    def wuerfeln(self):
        print "{0} würfelt".format(self)
        self.becher.wuerfeln()

    def aufdecken(self):
        print "{0} deckt auf".format(self)
        self.wuerfelList = self.becher.aufdecken()
        return self.wuerfelList

    def alleWuerfelAusBecherHolen(self):
        self.wuerfelList = becher.getAlleWuerfel()

    def getSpielerwuerfel(self):
        return self.wuerfelList

    def setSpielerwuerfel(self, wuerfelList):
        self.wuerfelList = wuerfelList

    def getBecher(self):
        return self.becher



