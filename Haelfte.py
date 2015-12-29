# coding=utf-8

from Config import Config
from Spieler import Spieler


class Haelfte(object):
    def __init__(self):
        self.strafsteine = Config.MAX_STRAFSTEINE
        self.runden = []
        self.verlierer = None

    def add_runde(self, runde):
        self.runden.append(runde)

    def get_aktuelle_rundennummer(self):
        return len(self.runden)

    def verteile_strafsteine(self, verlierer, anzahl):
        if anzahl >= self.strafsteine:
            anzahl = self.strafsteine

        verlierer.add_strafsteine(anzahl)
        self.strafsteine -= anzahl

    def has_strafsteine(self):
        return self.strafsteine > 0
