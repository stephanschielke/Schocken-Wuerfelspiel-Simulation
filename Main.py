# coding=utf-8

import random
from Spieler import Spieler
from Runde import Runde
from Zug import Zug
from Wurf import Wurf
from Ergebnis import Ergebnis

ANZAHL_SPIELER = 2
MAX_ANZAHL_WUERFE = 3

""" Spieler initialiseren """
spielerList = []
for x in xrange(0,ANZAHL_SPIELER):
    s = Spieler('Spieler {0}'.format(x+1))
    spielerList.append(s)
    print spielerList[x].name + ' nimmt teil.'

aktuellerSpieler = spielerList[0]
aktuelleRunde = Runde()
aktuellerZug = Zug(aktuellerSpieler)


""" Einen Zug spielen """
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





