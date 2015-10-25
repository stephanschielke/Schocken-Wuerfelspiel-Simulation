# coding=utf-8

from Wurf import Wurf
from Config import Config

class Runde(object):

    def __init__(self):
        self.zuege = []
        self.strafe = 0
        self.verlierer = None
        self.besterSpieler = None

    def addZug(self, zug):
        self.zuege.append(zug)

    def getZug(self, spieler):
        zug = None
        for x in xrange(0,len(self.zuege)):
            if self.zuege[x].spieler == spieler:
                zug = self.zuege[x]
        return zug

    def getErstenZug(self):
        return self.zuege[0]

    def getRundenBeginner(self):
        return self.zuege[0].spieler

    def getWinningWurf(self):
        """ TODO """
        return self.zuege[len(self.zuege)].getLastWurf()

    def getAktuelleZugNummer(self):
        return len(self.zuege)

    def ermittleStrafe(self):
        hoechsterZug = self.zuege[0]
        for x in xrange(1,len(self.zuege)):
            """ TODO: Mit-Ist-Shit """
            if hoechsterZug == None or self.zuege[x] > hoechsterZug :
                hoechsterZug = self.zuege[x]

        if Config.LOG_RUNDEN: print "Höchster Zug: {0}".format(hoechsterZug)

        if hoechsterZug != None :
            self.strafe = hoechsterZug.endergebnis.getStrafsteinWertigkeit()

        return self.strafe


    def ermittleBestenSpieler(self):
        hoechsterZug = self.zuege[0]
        for x in xrange(1,len(self.zuege)):
            """ TODO: Mit-Ist-Shit """
            if hoechsterZug == None or self.zuege[x] > hoechsterZug :
                hoechsterZug = self.zuege[x]

        if Config.LOG_RUNDEN: print "Bester Spieler der Runde: {0}".format(hoechsterZug.spieler)

        if hoechsterZug != None :
            self.besterSpieler = hoechsterZug.spieler

        return self.besterSpieler


    def ermittleVerlierer(self):
        niedrigsterZug = self.zuege[0]

        for x in xrange(1,len(self.zuege)):
            """ TODO: Mit-Ist-Shit """
            if niedrigsterZug == None or self.zuege[x] < niedrigsterZug :
                niedrigsterZug = self.zuege[x]

        if niedrigsterZug != None :
            self.verlierer = niedrigsterZug.spieler

        return self.verlierer