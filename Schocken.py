# coding=utf-8

""" Schocken module """

import random

from peewee import *
from playhouse.postgres_ext import *

from BaseModel import BaseModel

from Config import Config

""" Datenmodell
    n Spieler gehören zu n Spielen (Transformation?)
    1 Spieler besitzt 1 Becher
    1 Becher enthält 3 Würfel
    1 Würfel gehört zu 1 Becher

    1 Spiel besteht aus 2-3 Hälften
    1 Hälfte besteht aus n Runden
    1 Runde gehört zu 1 Hälfte
    1 Runde besteht aus n Zügen
    1 Zug gehört zu 1 Runde
    1 Zug besteht aus 1-3 Würfen
    1 Wurf gehört zu 1 Zug
    1 Zug gehört zu 1 Spieler
    1 Wurf hat 1 Ergebnis
    1 Ergebnis gehört zu 1 Wurf
"""

class Becher(BaseModel):

    def __init__(self):
        super(Becher, self).__init__()

        self.wuerfels = []

    def __str__(self):
        return "Würfelbecher enthält {0} Würfel".format(len(self.wuerfels))

    def befuellen(self, wuerfelList):
        for x in xrange(0,len(wuerfelList)):
            w = wuerfelList.pop();
            self.wuerfels.append(w)

    def befuelle(self, wuerfel):
        self.wuerfels.append(wuerfel)

    def wuerfeln(self):
        for x in xrange(0,len(self.wuerfels)):
            self.wuerfels[x].wuerfeln()

    def aufdecken(self):
        wuerfelList = []
        for x in xrange(0,len(self.wuerfels)):
            wuerfelList.append(self.wuerfels.pop())
        return wuerfelList

class Spieler(BaseModel):

    #ORM fields
    name = CharField(max_length=255, index=True, unique=True)
    becher = ForeignKeyField(Becher, related_name='becher', null=True)

    class Meta:
        database = Config.PSQL_DB

    def __init__(self, name):
        super(Spieler, self).__init__()

        self.name = name
        self.teilnehmend = True

        self.becher = Becher()
        self.becher.save()

        w1 = Wuerfel()
        w2 = Wuerfel()
        w3 = Wuerfel()

        w1.save()
        w2.save()
        w3.save()

        self.spielerWuerfel = [w1,w2,w3]
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
        self.spielerWuerfel.save()

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


class Wuerfel(BaseModel):

    augenzahl = IntegerField()

    def __init__(self):
        super(Wuerfel, self).__init__()

        self.augenzahl = random.randint(1,Config.WUERFELSEITEN)

    def __str__(self):
        return str(self.augenzahl)

    def wuerfeln(self):
        self.augenzahl = random.randint(1,Config.WUERFELSEITEN)

class Haelfte(BaseModel):

    #spiel = ForeignKeyField(Spiel, related_name='spiel')
    verlierer = ForeignKeyField(Spieler, related_name='verlierer', null=True)

    def __init__(self, spiel):
        super(Haelfte, self).__init__()

        self.spiel = spiel

        self.strafsteine = Config.MAX_STRAFSTEINE
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

class HaelfteField(Field):
    db_field = 'haelfte'

    def db_value(self, value):
        return value.id # convert HaelfteToRefId

    def python_value(self, value):
        return Haelfte.get(Haelfte.id == value)# convert id to Haelfte

class Spiel(BaseModel):

    #ORM fields
    nummer = IntegerField()
    #haelften = ArrayField(HaelfteField)

    def __init__(self, nummer):
        super(Spiel, self).__init__()

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

class Runde(BaseModel):

    strafe = IntegerField()
    verlierer = ForeignKeyField(Spieler, related_name='runden_verlierer', null=True)
    besterSpieler = ForeignKeyField(Spieler, related_name='runden_bester', null=True)

    def __init__(self):
        super(Runde, self).__init__()

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


class Ergebnis(BaseModel):

    isEndergebnis = BooleanField()

    # ORM fields
    auge_1 = IntegerField(null=True)
    auge_2 = IntegerField(null=True)
    auge_3 = IntegerField(null=True)

    def __init__(self, augen, isEndergebnis):
        super(Ergebnis, self).__init__()

        self.augen = sorted(augen, reverse=True)
        self.isEndergebnis = isEndergebnis

        #if self.isEndergebnis:
        if len(self.augen)>0:
            self.auge_1=self.augen[0]
        if len(self.augen)>1:
            self.auge_2=self.augen[1]
        if len(self.augen)>2:
            self.auge_3=self.augen[2]

    def __str__(self):
        return "[{0}]".format(",".join(str(x) for x in self.augen))

    def isSchock(self):
        einsen = [i for i in self.augen if i == 1]
        return len(einsen) >= 2

    def isSchockAus(self):
        einsen = [i for i in self.augen if i == 1]
        return len(einsen) >= 3

    def getStrafsteinWertigkeit(self):

        rangfolgeIndex = Config.RANGFOLGE.index(self);
        for x in xrange(0,len(Config.RANGFOLGE)):
            if self.augen == Config.RANGFOLGE[x]:
                rangfolgeIndex = x
                break

        #print "Gewinner-Ergebnis: {0} ".format(self)
        #print "Index: {0} ".format(rangfolgeIndex)

        if rangfolgeIndex == 0 :
            # Schock-Aus
            return 13
        elif rangfolgeIndex == 1 :
            return 6
        elif rangfolgeIndex == 2 :
            return 5
        elif rangfolgeIndex == 3 :
            return 4
        elif rangfolgeIndex == 4 :
            return 3
        elif rangfolgeIndex == 5 :
            return 2
        elif rangfolgeIndex >= 6 and rangfolgeIndex <= 10 :
            # Pushs
            return 3
        elif rangfolgeIndex >= 11 and rangfolgeIndex <= 13 :
            # Straßen
            return 2
        elif rangfolgeIndex >= 14:
            # Zahlen
            return 1

    def __lt__(self, other):
        return Config.RANGFOLGE.index(self) < Config.RANGFOLGE.index(other)

    def __le__(self, other):
        return Config.RANGFOLGE.index(self) <= Config.RANGFOLGE.index(other)

    def __eq__(self, other):
        same = True

        for x in xrange(0,len(self.augen)):
            same = self.augen[x] == other[x]
        return same

    def __ne__(self, other):
        return Config.RANGFOLGE.index(self) != Config.RANGFOLGE.index(other)

    def __gt__(self, other):
        return Config.RANGFOLGE.index(self) > Config.RANGFOLGE.index(other)

    def __ge__(self, other):
        return Config.RANGFOLGE.index(self) >= Config.RANGFOLGE.index(other)


class Zug(BaseModel):

    spieler = ForeignKeyField(Spieler, related_name='zug_spieler', null=True)
    endergebnis = ForeignKeyField(Ergebnis, related_name='endergebnis', null=True)

    def __init__(self, spieler):
        super(Zug, self).__init__()

        self.spieler = spieler
        self.wuerfe = []
        self.endergebnis = None

    def __str__(self):
        return "{0} mit Endergebnis {1}".format(self.spieler, self.endergebnis)

    def getLastWurf(self):
        return self.wuerfe[len(self.wuerfe)-1]

    def addWurf(self, wurf):
        self.wuerfe.append(wurf)

    def aktuellerWurf(self):
        return len(self.wuerfe)+1

    def __lt__(self, other):
        return self.endergebnis < other.endergebnis

    def __le__(self, other):
        return self.endergebnis <= other.endergebnis

    def __eq__(self, other):
        if other == None :
            return False
        return self.endergebnis == other.endergebnis

    def __ne__(self, other):
        if other == None :
            return True

        return self.endergebnis != other.endergebnis

    def __gt__(self, other):
        return self.endergebnis > other.endergebnis

    def __ge__(self, other):
        return self.endergebnis >= other.endergebnis


class Wurf(BaseModel):

    nummer = IntegerField()
    spieler = ForeignKeyField(Spieler, related_name='wurf_spieler', null=True)
    ergebnis = ForeignKeyField(Ergebnis, related_name='wurf_ergebnis', null=True)

    def __init__(self, nummer, spieler):
        super(Wurf, self).__init__()

        self.nummer = nummer
        self.spieler = spieler
        self.ergebnis = None

    def __str__(self):
        return "{0}. Wurf"

    def getSpielerWuerfel(self):
        return spieler.getSpielerwuerfel()

    def getErgebnis(self):
        self.ergebnis = Ergebnis([w.getAugenzahl() for w in spieler.getSpielerwuerfel()])
        return self.ergebnis

    def set_Ergebnis(self, ergebnis):
        self.ergebnis = ergebnis

        #if ergebnis.isEndergebnis:
            #self.ergebnis.save()


