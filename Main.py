# coding=utf-8

import random

from Spiel import Spiel
from Haelfte import Haelfte
from Runde import Runde
from Spieler import Spieler
from Zug import Zug
from Wurf import Wurf
from Ergebnis import Ergebnis

ANZAHL_SPIELER = 2
MAX_ANZAHL_WUERFE = 3
MAX_ANZAHL_HAELFTEN = 3
""" Ja, es kann 3 "Hälften" geben """

""" Spieler initialiseren """
spielerList = []
for x in xrange(0,ANZAHL_SPIELER):
    s = Spieler('Spieler {0}'.format(x+1))
    spielerList.append(s)
    print spielerList[x].name + ' nimmt teil.'
print

""" Ein neues Spiel beginnt """
aktuellesSpiel = Spiel()

while aktuellesSpiel.isEnde() == False :

    """ Die nächste Hälfte beginnt """
    print "======================="
    print "{0}. Hälfte hat begonnen.".format(aktuellesSpiel.getAktuelleHaelfteNummer()+1)
    print "======================="
    aktuelleHaelfte = Haelfte()

    """ Die Hälfte dauert so lange wie es keinen Verlierer gibt """
    while aktuelleHaelfte.getVerlierer() == None :

        """ Die nächste Runde beginnt """
        print "{0}. Runde hat begonnen.".format(aktuelleHaelfte.getAktuelleRundenNummer()+1)
        aktuelleRunde = Runde()

        for x in xrange(0,len(spielerList)):
            """ Nächster Spieler ist an der Reihe """
            aktuellerSpieler = spielerList[x]

            """ Einen Zug spielen """
            aktuellerZug = Zug(aktuellerSpieler)

            print "{0} ist am Zug".format(aktuellerSpieler)
            for wurfIndex in xrange(0, random.randint(1, MAX_ANZAHL_WUERFE)):

                print "{0} startet seinen {1}. Wurf".format(aktuellerSpieler, str(aktuellerZug.aktuellerWurf()))
                aktuellerWurf = Wurf(wurfIndex + 1, aktuellerSpieler)

                aufgedeckteWuerfel = aktuellerSpieler.getSpielerwuerfel()

                if wurfIndex+1 == 1 :
                    """ Beim ersten Wurf werden alle Würfel in den becher getan """
                    anzahlZuerueckgelegt = aktuellerSpieler.alleWuerfelInBecherLegen()
                else:
                    """ Ansonsten random Anzahl wieder in den Becher """
                    anzahlZuerueckgelegt = aktuellerSpieler.randomWuerfelInBecherLegen()

                tischErgebnis = Ergebnis([w.getAugenzahl() for w in aktuellerSpieler.getSpielerwuerfel()])
                print "Tisch: {0}".format(tischErgebnis)

                if anzahlZuerueckgelegt == 0 or (wurfIndex == 2 and aktuellerSpieler == spielerList[0]):
                    """ Spieler will nicht mehr würfeln und lässt stehen """
                    print "{0} lässt stehen.".format(aktuellerSpieler)
                    break
                else:
                    """ Spieler will weiterwürfeln """
                    aktuellerSpieler.wuerfeln()
                    aufgedeckteWuerfel = aktuellerSpieler.aufdecken()

                wurfErgebnis = Ergebnis([w.getAugenzahl() for w in aufgedeckteWuerfel])

                print "Wurf: {0}".format(wurfErgebnis)

                gesamtErgebnis = Ergebnis(tischErgebnis.getAugen() + wurfErgebnis.getAugen())

                aktuellerWurf.setErgebnis(gesamtErgebnis)

                aktuellerZug.addWurf(aktuellerWurf)

            # Würfe von Spieler X sind vorbei

            print "{0} beendet seinen Zug".format(aktuellerSpieler)

            aktuellerZug.setEndergebnis(gesamtErgebnis)
            print "Zugergebnis: {0}".format(gesamtErgebnis)

            #if gesamtErgebnis.isMeierAus() :
            #    break

            aktuelleRunde.addZug(aktuellerZug)

            # Zug vom Spieler X ist vorbei

        # Alle Spieler haben Ihre Züge gemacht.

        # Spieler der angefangen hat muss noch aufdecken
        rundenBeginner = spielerList[0]
        #print "Spieler {0} enthüllt:".format(rundenBeginner)
        aufgedeckteWuerfel = rundenBeginner.aufdecken()
        wurfErgebnis = Ergebnis([w.getAugenzahl() for w in aufgedeckteWuerfel])
        print "Zugergebnis: {0}".format(wurfErgebnis)
        gesamtErgebnis = Ergebnis(rundenBeginner.getSpielerwuerfel() + wurfErgebnis.getAugen())
        aktuelleRunde.getErstenZug().getLastWurf().setErgebnis(gesamtErgebnis)

        # Runde ist vorbei.

        rundenVerlierer = aktuelleRunde.ermittleVerlierer()
        rundenBester = aktuelleRunde.ermittleBestenSpieler()
        strafe = aktuelleRunde.ermittleStrafe()
        aktuelleHaelfte.addRunde(aktuelleRunde)
        print "Die {0}. Runde hat {1} verloren.".format(aktuelleHaelfte.getAktuelleRundenNummer(), rundenVerlierer)
        print

        for x in xrange(0,len(spielerList)):
            print "{0} hat {1} Strafsteine".format(spielerList[x], spielerList[x].getStrafsteine())

        # Strafsteine verteilen
        if aktuelleHaelfte.hasStrafsteine() :
            print "Auf dem Stapel befinden sich {0} Strafsteine".format(aktuelleHaelfte.getStrafsteine())
            print "{0} bekommt {1} Straftsteine vom Stapel".format(rundenVerlierer, strafe)
            aktuelleHaelfte.verteileStrafsteine(rundenVerlierer, strafe)
            print "Auf dem Stapel befinden sich jetzt {0} Strafsteine".format(aktuelleHaelfte.getStrafsteine())
        else :
            print "Auf dem Stapel befinden sich keine Strafsteine mehr."
            print "{0} bekommt {1} Straftsteine von {2}".format(rundenVerlierer, strafe, rundenBester)
            verteilteSteine = rundenBester.verteileStrafsteine(rundenVerlierer, strafe)
            print "{0} hat {1} Straftsteine von {2} bekommen".format(rundenVerlierer, verteilteSteine, rundenBester)

        # Gibt es einen Verlierer?
        for x in xrange(0,len(spielerList)):
            spieler = spielerList[x]
            print "{0} hat jetzt {1} Strafsteine".format(spieler, spieler.getStrafsteine())
            if spieler.hasHaelfteVerloren():
                aktuelleHaelfte.setVerlierer(spieler)

    # Eine Hälfte ist vorbei
    aktuellesSpiel.addHaelfte(aktuelleHaelfte)

    for x in xrange(0,len(spielerList)):
        spielerList[x].eraseStrafsteine()



    print
    print "Die {0}. Hälfte hat {1} verloren.".format(aktuellesSpiel.getAktuelleHaelfteNummer(), aktuelleHaelfte.getVerlierer())
    print
print "=================="
print "Das Spiel ist aus."
print "=================="
print
print "{0} hat verloren und muss eine Runde ausgeben.".format(aktuellesSpiel.getVerlierer())
print



