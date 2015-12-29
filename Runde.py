# coding=utf-8

from Config import Config


class Runde(object):
    def __init__(self):
        self.zuege = []
        self.strafe = 0
        self.verlierer = None
        self.besterSpieler = None

    def add_zug(self, zug):
        self.zuege.append(zug)

    def get_zug(self, spieler):
        zug = None
        for x in range(0, len(self.zuege)):
            if self.zuege[x].spieler == spieler:
                zug = self.zuege[x]
        return zug

    def get_ersten_zug(self):
        return self.zuege[0]

    def get_runden_beginner(self):
        return self.zuege[0].spieler

    def get_winning_wurf(self):
        """ TODO """
        return self.zuege[len(self.zuege)].get_last_wurf()

    def get_aktuelle_zugnummer(self):
        return len(self.zuege)

    def ermittle_strafe(self):
        hoechster_zug = self.zuege[0]
        for x in range(1, len(self.zuege)):
            """ TODO: Mit-Ist-Shit """
            if hoechster_zug is None or self.zuege[x] > hoechster_zug:
                hoechster_zug = self.zuege[x]

        if Config.LOG_RUNDEN: print("Höchster Zug: {0}".format(hoechster_zug))

        if hoechster_zug is not None:
            self.strafe = hoechster_zug.endergebnis.get_strafstein_wertigkeit()

        return self.strafe

    def ermittle_besten_spieler(self):
        hoechster_zug = self.zuege[0]
        for x in range(1, len(self.zuege)):
            """ TODO: Mit-Ist-Shit """
            if hoechster_zug is None or self.zuege[x] > hoechster_zug:
                hoechster_zug = self.zuege[x]

        if Config.LOG_RUNDEN: print("Bester Spieler der Runde: {0}".format(hoechster_zug.spieler))

        if hoechster_zug is not None:
            self.besterSpieler = hoechster_zug.spieler

        return self.besterSpieler

    def ermittle_verlierer(self):
        niedrigster_zug = self.zuege[0]

        for x in range(1, len(self.zuege)):
            """ TODO: Mit-Ist-Shit """
            if niedrigster_zug is None or self.zuege[x] < niedrigster_zug:
                niedrigster_zug = self.zuege[x]

        if niedrigster_zug is not None:
            self.verlierer = niedrigster_zug.spieler

        return self.verlierer
