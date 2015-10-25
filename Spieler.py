# coding=utf-8

import random
from Config import Config
from Becher import Becher
from Wuerfel import Wuerfel
from Haelfte import Haelfte

class Spieler(object):

    def __init__(self, name):
        self.name = name
        self.teilnehmend = True
        self.becher = Becher(self)
        self.spielerWuerfel = [Wuerfel(),Wuerfel(),Wuerfel()]
        self.strafsteine = 0
        self.markierungsstein = 0

    def __str__(self):
        return self.name

    def alleWuerfelInBecherLegen(self):
        anzahlInBecherGelegt = len(self.spielerWuerfel)
        if Config.LOG_WUERFE: print "{0} legt {1} Würfel in den Becher.".format(self, anzahlInBecherGelegt)
        self.becher.befuellen(self.spielerWuerfel)
        return anzahlInBecherGelegt

    def randomWuerfelInBecherLegen(self):
        r = random.randint(0,len(self.spielerWuerfel))
        if r != 0 :
            if Config.LOG_WUERFE: print "{0} legt {1} Würfel zurück in den Becher.".format(self, r)
            for x in xrange(0,r):
                w = self.spielerWuerfel.pop(random.randrange(len(self.spielerWuerfel)))
                self.becher.befuelle(w)
        else:
            if Config.LOG_WUERFE: print "{0} legt keine Würfel zurück in den Becher.".format(self)

        return r

    def wuerfeln(self):
        if Config.LOG_WUERFE: print "{0} würfelt".format(self)
        self.becher.wuerfeln()

    def aufdecken(self):
        if Config.LOG_WUERFE: print "{0} deckt auf".format(self)
        aufgedeckteWuerfel = self.becher.aufdecken();
        self.spielerWuerfel = sorted(self.spielerWuerfel + aufgedeckteWuerfel)
        return aufgedeckteWuerfel

    def alleWuerfelAusBecherHolen(self):
        self.spielerWuerfel = becher.getAlleWuerfel()

    def addStrafsteine(self, anzahl):
        self.strafsteine += anzahl

    def hasStrafsteine(self):
        return self.strafsteine > 0

    def eraseStrafsteine(self):
        self.strafsteine = 0

    def eraseMarkierungsstein(self):
        self.markierungsstein = 0

    def verteileStrafsteine(self, verlierer, anzahl):
        if anzahl >= self.strafsteine:
            anzahl = self.strafsteine

        verlierer.addStrafsteine(anzahl)
        self.strafsteine -= anzahl

        return anzahl

    def hasHaelfteVerloren(self):
        return self.strafsteine >= Config.MAX_STRAFSTEINE

    def hasMarkierungsstein(self):
        return self.markierungsstein > 0

    def addMarkierungsstein(self):
        self.markierungsstein += 1



