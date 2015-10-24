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
for x in xrange(0,random.randint(1,MAX_ANZAHL_WUERFE)):

    print "{0} startet seinen {1}. Wurf".format(aktuellerSpieler, str(aktuellerZug.aktuellerWurf()))
    aktuellerWurf = Wurf(x+1, aktuellerSpieler)

    aktuellerSpieler.alleWuerfelInBecherLegen()


    aktuellerSpieler.wuerfeln()



    offeneWuerfel = aktuellerSpieler.aufdecken()
    ergebnis = Ergebnis([w.getAugenzahl() for w in offeneWuerfel])
    print ergebnis

    aktuellerZug.addWurf(aktuellerWurf)

print "{0} beendet seinen Zug".format(aktuellerSpieler)


