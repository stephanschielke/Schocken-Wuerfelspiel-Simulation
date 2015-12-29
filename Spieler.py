# coding=utf-8

import random

from Config import Config
from Becher import Becher
from Wuerfel import Wuerfel


class Spieler(object):
    def __init__(self, name):
        self.name = name
        self.teilnehmend = True
        self.becher = Becher(self)
        self.spielerWuerfel = [Wuerfel(), Wuerfel(), Wuerfel()]
        self.strafsteine = 0
        self.markierungsstein = 0

    def __str__(self):
        return self.name

    def alle_wuerfel_in_becher_legen(self):
        anzahl_in_becher_gelegt = len(self.spielerWuerfel)
        if Config.LOG_WUERFE: print("{0} legt {1} Würfel in den Becher.".format(self, anzahl_in_becher_gelegt))
        self.becher.befuellen(self.spielerWuerfel)
        return anzahl_in_becher_gelegt

    def random_wuerfel_in_becher_legen(self):
        r = random.randint(0, len(self.spielerWuerfel))
        if r != 0:
            if Config.LOG_WUERFE: print("{0} legt {1} Würfel zurück in den Becher.".format(self, r))
            for x in range(0, r):
                w = self.spielerWuerfel.pop(random.randrange(len(self.spielerWuerfel)))
                self.becher.befuelle(w)
        else:
            if Config.LOG_WUERFE: print("{0} legt keine Würfel zurück in den Becher.".format(self))

        return r

    def wuerfeln(self):
        if Config.LOG_WUERFE: print("{0} würfelt".format(self))
        self.becher.wuerfeln()

    def aufdecken(self):
        if Config.LOG_WUERFE: print("{0} deckt auf".format(self))
        aufgedeckte_wuerfel = self.becher.aufdecken();
        self.spielerWuerfel = sorted(self.spielerWuerfel + aufgedeckte_wuerfel)
        return aufgedeckte_wuerfel

    def alle_wuerfel_aus_becher_holen(self):
        self.spielerWuerfel = becher.getAlleWuerfel()

    def add_strafsteine(self, anzahl):
        self.strafsteine += anzahl

    def has_strafsteine(self):
        return self.strafsteine > 0

    def erase_strafsteine(self):
        self.strafsteine = 0

    def erase_markierungsstein(self):
        self.markierungsstein = 0

    def verteile_strafsteine(self, verlierer, anzahl):
        if anzahl >= self.strafsteine:
            anzahl = self.strafsteine

        verlierer.add_strafsteine(anzahl)
        self.strafsteine -= anzahl

        return anzahl

    def has_haelfte_verloren(self):
        return self.strafsteine >= Config.MAX_STRAFSTEINE

    def has_markierungsstein(self):
        return self.markierungsstein > 0

    def add_markierungsstein(self):
        self.markierungsstein += 1
