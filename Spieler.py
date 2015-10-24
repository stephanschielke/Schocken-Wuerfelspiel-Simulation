# coding=utf-8

import random
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
        anzahlInBecherGelegt = len(self.wuerfelList)
        print "{0} legt {1} Würfel in den Becher.".format(self, anzahlInBecherGelegt)
        self.becher.befuellen(self.wuerfelList)
        return anzahlInBecherGelegt

    def randomWuerfelInBecherLegen(self):
        r = random.randint(0,len(self.wuerfelList))
        if r != 0 :
            print "{0} legt {1} Würfel zurück in den Becher.".format(self, r)
            for x in xrange(0,r):
                w = self.wuerfelList.pop(random.randrange(len(self.wuerfelList)))
                self.becher.befuelle(w)
        else:
            print "{0} legt keine Würfel zurück in den Becher.".format(self)

        return r

    def wuerfeln(self):
        print "{0} würfelt".format(self)
        self.becher.wuerfeln()

    def aufdecken(self):
        print "{0} deckt auf".format(self)
        aufgedeckteWuerfel = self.becher.aufdecken();
        self.wuerfelList = sorted(self.wuerfelList + aufgedeckteWuerfel)
        return aufgedeckteWuerfel

    def alleWuerfelAusBecherHolen(self):
        self.wuerfelList = becher.getAlleWuerfel()

    def getSpielerwuerfel(self):
        return self.wuerfelList

    def setSpielerwuerfel(self, wuerfelList):
        self.wuerfelList = wuerfelList

    def getBecher(self):
        return self.becher



