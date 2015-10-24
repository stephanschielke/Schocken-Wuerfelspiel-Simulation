# coding=utf-8

import random

from Spiel import Spiel
from Haelfte import Haelfte
from Runde import Runde
from Spieler import Spieler
from Zug import Zug
from Wurf import Wurf
from Ergebnis import Ergebnis

ANZAHL_SPIELER = 3
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
    print "{0}. Hälfte hat begonnen.".format(aktuellesSpiel.getAktuelleHaelfteNummer()+1)
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

                if anzahlZuerueckgelegt == 0 :
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

            print "{0} beendet seinen Zug".format(aktuellerSpieler)

            print "Zugergebnis: {0}".format(gesamtErgebnis)

            if gesamtErgebnis.isMeierAus() :
                aktuelleHaelfte.setVerlierer(aktuellerSpieler)
                break

            aktuelleRunde.addZug(aktuellerZug)

        aktuelleHaelfte.addRunde(aktuelleRunde)

        if gesamtErgebnis.isMeierAus() :
            break

    aktuelleHaelfte.setVerlierer(aktuellerSpieler)

    aktuellesSpiel.addHaelfte(aktuelleHaelfte)

print "Das Spiel ist aus. Es hat {0} Hälften gedauert.".format(aktuellesSpiel.getAktuelleHaelfteNummer())
print "Verloren hat {0}.".format(aktuellesSpiel.getVerlierer())


