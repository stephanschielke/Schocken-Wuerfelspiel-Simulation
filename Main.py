# coding=utf-8

import random

from Config import Config
from Spieler import Spieler
from Spiel import Spiel
from Haelfte import Haelfte
from Runde import Runde
from Zug import Zug
from Wurf import Wurf
from Ergebnis import Ergebnis

"""
TODOs:  zwei Sechsen zu einer Eins umdrehen, wenn danach noch ein Wurf frei ist.
        Mit-Ist-Shit-Regel beachten
        Handwürfe > zusammengewürfelte Würfe
"""

""" Spieler initialiseren """
passiveSpieler = []
aktiveSpieler = []
for x in xrange(0,Config.ANZAHL_SPIELER):
    s = Spieler('Spieler {0}'.format(x+1))
    aktiveSpieler.append(s)

    if Config.LOG_SPIEL: print aktiveSpieler[x].name + ' nimmt teil.'
if Config.LOG_SPIEL: print

for x in xrange(1,Config.ANZAHL_SPIELE+1):
    """ Ein neues Spiel beginnt """
    if Config.LOG_SPIEL: print "====================="
    if Config.LOG_SPIEL: print "     Spielbeginn     "
    if Config.LOG_SPIEL: print "====================="
    aktuellesSpiel = Spiel(x)

    while aktuellesSpiel.isEnde() == False :

        """ Die nächste Hälfte beginnt """
        if Config.LOG_HAELFTEN: print "======================="
        if Config.LOG_HAELFTEN: print "{0}. Hälfte hat begonnen.".format(aktuellesSpiel.getAktuelleHaelfteNummer()+1)
        if Config.LOG_HAELFTEN: print "======================="
        aktuelleHaelfte = Haelfte()

        # Alle nehmen bei einer neuen Hälfte Teil
        for x in xrange(len(passiveSpieler)-1, -1, -1):
            spieler = passiveSpieler[x]
            passiveSpieler.remove(spieler)
            aktiveSpieler.append(spieler)

        # Spieler aus dem Finale nehmen wenn sie keine Hälfte haben
        if aktuellesSpiel.getAktuelleHaelfteNummer() == Config.MAX_ANZAHL_WUERFE-1:
            for x in xrange(len(aktiveSpieler)-1, -1, -1):
                spieler = aktiveSpieler[x]
                #print "{0} aktive Spieler".format(len(aktiveSpieler))

                #print "{0} Strafsteine".format(spieler.strafsteine)
                #print "{0} Haelften".format(spieler.haelfte)
                if spieler.hasMarkierungsstein():
                    if Config.LOG_HAELFTEN: print "{0} nimmt an dieser Hälfte teil.".format(spieler)
                else:
                    if Config.LOG_HAELFTEN: print "{0} ist raus aus dem Finale.".format(spieler)
                    aktiveSpieler.remove(spieler)
                    passiveSpieler.append(spieler)

                #print "{0} aktive Spieler".format(len(aktiveSpieler))

        for x in xrange(len(aktiveSpieler)-1, -1, -1):
            if Config.LOG_HAELFTEN: print "{0} nimmt an dieser Hälfte teil.".format(aktiveSpieler[x])

        if Config.LOG_HAELFTEN: print

        """ Die Hälfte dauert so lange wie es keinen Verlierer gibt """
        while aktuelleHaelfte.verlierer == None :

            """ Die nächste Runde beginnt """
            if Config.LOG_RUNDEN: print
            if Config.LOG_RUNDEN: print "{0}. Runde hat begonnen.".format(aktuelleHaelfte.getAktuelleRundenNummer()+1)
            aktuelleRunde = Runde()

            # Spieler aus dem Finale nehmen wenn sie keine Hälfte haben
            #print "{0} aktive Spieler".format(len(aktiveSpieler))

            for x in xrange(len(aktiveSpieler)-1,-1,-1):
                spieler = aktiveSpieler[x]
                if not aktuelleHaelfte.hasStrafsteine() and not spieler.hasStrafsteine():
                    if Config.LOG_RUNDEN: print "{0} ist raus aus der Runde.".format(spieler)
                    aktiveSpieler.remove(spieler)
                    passiveSpieler.append(spieler)
                else:
                    if Config.LOG_RUNDEN: print "{0} nimmt an dieser Runde teil.".format(spieler)

            #print "{0} aktive Spieler".format(len(aktiveSpieler))

            if Config.LOG_RUNDEN: print

            for x in xrange(0,len(aktiveSpieler)):
                """ Nächster Spieler ist an der Reihe """
                aktuellerSpieler = aktiveSpieler[x]

                """ Einen Zug spielen """
                aktuellerZug = Zug(aktuellerSpieler)

                if Config.LOG_ZUEGE: print "{0} ist am Zug".format(aktuellerSpieler)
                for wurfIndex in xrange(0, random.randint(1, Config.MAX_ANZAHL_WUERFE)):

                    if Config.LOG_WUERFE: print "{0} startet seinen {1}. Wurf".format(aktuellerSpieler, str(aktuellerZug.aktuellerWurf()))
                    aktuellerWurf = Wurf(wurfIndex + 1, aktuellerSpieler)

                    aufgedeckteWuerfel = aktuellerSpieler.spielerWuerfel

                    if wurfIndex+1 == 1 :
                        """ Beim ersten Wurf werden alle Würfel in den becher getan """
                        anzahlZuerueckgelegt = aktuellerSpieler.alleWuerfelInBecherLegen()
                    else:
                        """ Ansonsten random Anzahl wieder in den Becher """
                        anzahlZuerueckgelegt = aktuellerSpieler.randomWuerfelInBecherLegen()

                    tischErgebnis = Ergebnis([w.augenzahl for w in aktuellerSpieler.spielerWuerfel])
                    if Config.LOG_WUERFE: print "Tisch: {0}".format(tischErgebnis)

                    if anzahlZuerueckgelegt == 0 or (wurfIndex == Config.MAX_ANZAHL_WUERFE-1 and aktuellerSpieler == aktiveSpieler[0]):
                        """ Spieler will nicht mehr würfeln und lässt stehen """
                        if Config.LOG_WUERFE: print "{0} lässt stehen.".format(aktuellerSpieler)
                        break
                    else:
                        """ Spieler will weiterwürfeln """
                        aktuellerSpieler.wuerfeln()
                        aufgedeckteWuerfel = aktuellerSpieler.aufdecken()

                    wurfErgebnis = Ergebnis([w.augenzahl for w in aufgedeckteWuerfel])

                    if Config.LOG_WUERFE: print "Wurf: {0}".format(wurfErgebnis)

                    gesamtErgebnis = Ergebnis(tischErgebnis.augen + wurfErgebnis.augen)
                    aktuellerWurf.set_Ergebnis(gesamtErgebnis)

                    aktuellerZug.addWurf(aktuellerWurf)

                # Würfe von Spieler X sind vorbei

                if Config.LOG_ZUEGE: print "{0} beendet seinen Zug".format(aktuellerSpieler)

                aktuellerZug.endergebnis = gesamtErgebnis
                if Config.LOG_ZUEGE: print "Zugergebnis: {0}".format(gesamtErgebnis)

                aktuelleRunde.addZug(aktuellerZug)

                if gesamtErgebnis.isSchockAus() :
                    break

                # Zug vom Spieler X ist vorbei

            # Alle Spieler haben Ihre Züge gemacht.

            # Spieler der angefangen hat muss noch aufdecken
            rundenBeginner = aktiveSpieler[0]
            if len(rundenBeginner.spielerWuerfel) != 3:
                #print "Spieler {0} enthüllt:".format(rundenBeginner)
                aufgedeckteWuerfel = rundenBeginner.aufdecken()
                wurfErgebnis = Ergebnis([w.augenzahl for w in aufgedeckteWuerfel])
                if Config.LOG_ZUEGE: print "Zugergebnis: {0}".format(wurfErgebnis)
                gesamtErgebnis = Ergebnis(rundenBeginner.spielerWuerfel + wurfErgebnis.augen)
                aktuelleRunde.getErstenZug().getLastWurf().set_Ergebnis(gesamtErgebnis)

            # Runde ist vorbei.

            rundenVerlierer = aktuelleRunde.ermittleVerlierer()
            rundenBester = aktuelleRunde.ermittleBestenSpieler()
            strafe = aktuelleRunde.ermittleStrafe()
            aktuelleHaelfte.addRunde(aktuelleRunde)
            if Config.LOG_RUNDEN: print "Die {0}. Runde hat {1} verloren.".format(aktuelleHaelfte.getAktuelleRundenNummer(), rundenVerlierer)
            if Config.LOG_RUNDEN: print

            for x in xrange(0,len(aktiveSpieler)):
                if Config.LOG_STRAFSTEINE: print "{0} hat {1} Strafsteine".format(aktiveSpieler[x], aktiveSpieler[x].strafsteine)

            # Strafsteine verteilen
            if aktuelleHaelfte.hasStrafsteine() :
                if Config.LOG_STRAFSTEINE: print "Auf dem Stapel befinden sich {0} Strafsteine".format(aktuelleHaelfte.strafsteine)
                if Config.LOG_STRAFSTEINE: print "{0} bekommt {1} Straftsteine vom Stapel".format(rundenVerlierer, strafe)
                aktuelleHaelfte.verteileStrafsteine(rundenVerlierer, strafe)
            else :
                if Config.LOG_STRAFSTEINE: print "Auf dem Stapel befinden sich keine Strafsteine mehr."
                if Config.LOG_STRAFSTEINE: print "{0} bekommt {1} Straftsteine von {2}".format(rundenVerlierer, strafe, rundenBester)
                verteilteSteine = rundenBester.verteileStrafsteine(rundenVerlierer, strafe)

            if gesamtErgebnis.isSchockAus() :
                aktuelleHaelfte.verlierer = rundenVerlierer
                rundenVerlierer.addMarkierungsstein()
            else:
                # Gibt es einen Verlierer?
                for x in xrange(0,len(aktiveSpieler)):
                    spieler = aktiveSpieler[x]
                    if spieler.hasHaelfteVerloren():
                        if Config.LOG_STRAFSTEINE: print "{0} hat jetzt {1} Strafsteine".format(spieler, spieler.strafsteine)
                        aktuelleHaelfte.verlierer = spieler
                        spieler.addMarkierungsstein()

        # Eine Hälfte ist vorbei
        aktuellesSpiel.addHaelfte(aktuelleHaelfte)
        if Config.LOG_HAELFTEN: print
        if Config.LOG_HAELFTEN: print "Die {0}. Hälfte hat {1} verloren.".format(aktuellesSpiel.getAktuelleHaelfteNummer(), aktuelleHaelfte.verlierer)
        if Config.LOG_HAELFTEN: print

        # Verlierer muss in der nächsten Runde anfangen
        verlierer = aktiveSpieler.pop(aktiveSpieler.index(aktuelleHaelfte.verlierer))
        aktiveSpieler.insert(0, verlierer)

        # Spielsteine zurücksetzen
        for x in xrange(0,len(aktiveSpieler)):
            aktiveSpieler[x].eraseStrafsteine()

    # Markierungssteine löschen
    for x in xrange(0,len(aktiveSpieler)):
        aktiveSpieler[x].eraseMarkierungsstein()

    if Config.LOG_SPIEL: print "====================="
    if Config.LOG_SPIEL: print "Das {0}. Spiel ist aus".format(aktuellesSpiel.nummer)
    if Config.LOG_SPIEL: print "====================="
    if Config.LOG_SPIEL: print
    if Config.LOG_SPIEL: print "{0} hat verloren und muss eine Runde ausgeben!".format(aktuellesSpiel.getVerlierer())
    if Config.LOG_SPIEL: print




