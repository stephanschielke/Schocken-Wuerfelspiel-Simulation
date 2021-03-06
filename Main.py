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
for x in range(0, Config.ANZAHL_SPIELER):
    s = Spieler('Spieler {0}'.format(x + 1))
    aktiveSpieler.append(s)

    if Config.LOG_SPIEL: print(aktiveSpieler[x].name + ' nimmt teil.')
if Config.LOG_SPIEL: print()

for x in range(1, Config.ANZAHL_SPIELE + 1):
    """ Ein neues Spiel beginnt """
    if Config.LOG_SPIEL: print("=====================")
    if Config.LOG_SPIEL: print("     Spielbeginn     ")
    if Config.LOG_SPIEL: print("=====================")
    aktuellesSpiel = Spiel(x)

    while not aktuellesSpiel.is_ende():

        """ Die nächste Hälfte beginnt """
        if Config.LOG_HAELFTEN: print("=======================")
        if Config.LOG_HAELFTEN: print(
            "{0}. Hälfte hat begonnen.".format(aktuellesSpiel.get_aktuelle_haelfte_nummer() + 1))
        if Config.LOG_HAELFTEN: print("=======================")
        aktuelleHaelfte = Haelfte()

        # Alle nehmen bei einer neuen Hälfte Teil
        for x in range(len(passiveSpieler) - 1, -1, -1):
            spieler = passiveSpieler[x]
            passiveSpieler.remove(spieler)
            aktiveSpieler.append(spieler)

        # Spieler aus dem Finale nehmen wenn sie keine Hälfte haben
        if aktuellesSpiel.get_aktuelle_haelfte_nummer() == Config.MAX_ANZAHL_WUERFE - 1:
            for x in range(len(aktiveSpieler) - 1, -1, -1):
                spieler = aktiveSpieler[x]
                # print "{0} aktive Spieler".format(len(aktiveSpieler))

                # print "{0} Strafsteine".format(spieler.strafsteine)
                # print "{0} Haelften".format(spieler.haelfte)
                if spieler.has_markierungsstein():
                    if Config.LOG_HAELFTEN: print("{0} nimmt an dieser Hälfte teil.".format(spieler))
                else:
                    if Config.LOG_HAELFTEN: print("{0} ist raus aus dem Finale.".format(spieler))
                    aktiveSpieler.remove(spieler)
                    passiveSpieler.append(spieler)

                    # print "{0} aktive Spieler".format(len(aktiveSpieler))

        for x in range(len(aktiveSpieler) - 1, -1, -1):
            if Config.LOG_HAELFTEN: print("{0} nimmt an dieser Hälfte teil.".format(aktiveSpieler[x]))

        if Config.LOG_HAELFTEN: print()

        """ Die Hälfte dauert so lange wie es keinen Verlierer gibt """
        while aktuelleHaelfte.verlierer is None:

            """ Die nächste Runde beginnt """
            if Config.LOG_RUNDEN: print()
            if Config.LOG_RUNDEN: print(
                "{0}. Runde hat begonnen.".format(aktuelleHaelfte.get_aktuelle_rundennummer() + 1))
            aktuelleRunde = Runde()

            # Spieler aus dem Finale nehmen wenn sie keine Hälfte haben
            # print "{0} aktive Spieler".format(len(aktiveSpieler))

            for x in range(len(aktiveSpieler) - 1, -1, -1):
                spieler = aktiveSpieler[x]
                if not aktuelleHaelfte.has_strafsteine() and not spieler.has_strafsteine():
                    if Config.LOG_RUNDEN: print("{0} ist raus aus der Runde.".format(spieler))
                    aktiveSpieler.remove(spieler)
                    passiveSpieler.append(spieler)
                else:
                    if Config.LOG_RUNDEN: print("{0} nimmt an dieser Runde teil.".format(spieler))

            # print "{0} aktive Spieler".format(len(aktiveSpieler))

            if Config.LOG_RUNDEN: print()

            for x in range(0, len(aktiveSpieler)):
                """ Nächster Spieler ist an der Reihe """
                aktuellerSpieler = aktiveSpieler[x]

                """ Einen Zug spielen """
                aktuellerZug = Zug(aktuellerSpieler)

                if Config.LOG_ZUEGE: print("{0} ist am Zug".format(aktuellerSpieler))
                for wurfIndex in range(0, random.randint(1, Config.MAX_ANZAHL_WUERFE)):

                    if Config.LOG_WUERFE: print(
                        "{0} startet seinen {1}. Wurf".format(aktuellerSpieler, str(aktuellerZug.aktueller_wurf())))
                    aktuellerWurf = Wurf(wurfIndex + 1, aktuellerSpieler)

                    aufgedeckteWuerfel = aktuellerSpieler.spielerWuerfel

                    if wurfIndex + 1 == 1:
                        """ Beim ersten Wurf werden alle Würfel in den becher getan """
                        anzahlZuerueckgelegt = aktuellerSpieler.alle_wuerfel_in_becher_legen()
                    else:
                        """ Ansonsten random Anzahl wieder in den Becher """
                        anzahlZuerueckgelegt = aktuellerSpieler.random_wuerfel_in_becher_legen()

                    tischErgebnis = Ergebnis([w.augenzahl for w in aktuellerSpieler.spielerWuerfel])
                    if Config.LOG_WUERFE: print("Tisch: {0}".format(tischErgebnis))

                    if anzahlZuerueckgelegt == 0 or (
                            wurfIndex == Config.MAX_ANZAHL_WUERFE - 1 and aktuellerSpieler == aktiveSpieler[0]):
                        """ Spieler will nicht mehr würfeln und lässt stehen """
                        if Config.LOG_WUERFE: print("{0} lässt stehen.".format(aktuellerSpieler))
                        break
                    else:
                        """ Spieler will weiterwürfeln """
                        aktuellerSpieler.wuerfeln()
                        aufgedeckteWuerfel = aktuellerSpieler.aufdecken()

                    wurfErgebnis = Ergebnis([w.augenzahl for w in aufgedeckteWuerfel])

                    if Config.LOG_WUERFE: print("Wurf: {0}".format(wurfErgebnis))

                    gesamtErgebnis = Ergebnis(tischErgebnis.augen + wurfErgebnis.augen)
                    aktuellerWurf.set_ergebnis(gesamtErgebnis)

                    aktuellerZug.add_wurf(aktuellerWurf)

                # Würfe von Spieler X sind vorbei

                if Config.LOG_ZUEGE: print("{0} beendet seinen Zug".format(aktuellerSpieler))

                aktuellerZug.endergebnis = gesamtErgebnis
                if Config.LOG_ZUEGE: print("Zugergebnis: {0}".format(gesamtErgebnis))

                aktuelleRunde.add_zug(aktuellerZug)

                if gesamtErgebnis.is_schock_aus():
                    break

                    # Zug vom Spieler X ist vorbei

            # Alle Spieler haben Ihre Züge gemacht.

            # Spieler der angefangen hat muss noch aufdecken
            rundenBeginner = aktiveSpieler[0]
            if len(rundenBeginner.spielerWuerfel) != 3:
                # print "Spieler {0} enthüllt:".format(rundenBeginner)
                aufgedeckteWuerfel = rundenBeginner.aufdecken()
                wurfErgebnis = Ergebnis([w.augenzahl for w in aufgedeckteWuerfel])

                if Config.LOG_ZUEGE: print("Zugergebnis: {0}".format(wurfErgebnis))

                gesamtErgebnis = Ergebnis(rundenBeginner.spielerWuerfel + aufgedeckteWuerfel)
                aktuelleRunde.get_ersten_zug().get_last_wurf().set_ergebnis(gesamtErgebnis)

            # Runde ist vorbei.

            rundenVerlierer = aktuelleRunde.ermittle_verlierer()
            rundenBester = aktuelleRunde.ermittle_besten_spieler()
            strafe = aktuelleRunde.ermittle_strafe()
            aktuelleHaelfte.add_runde(aktuelleRunde)
            if Config.LOG_RUNDEN: print(
                "Die {0}. Runde hat {1} verloren.".format(aktuelleHaelfte.get_aktuelle_rundennummer(), rundenVerlierer))
            if Config.LOG_RUNDEN: print()

            for x in range(0, len(aktiveSpieler)):
                if Config.LOG_STRAFSTEINE: print(
                    "{0} hat {1} Strafsteine".format(aktiveSpieler[x], aktiveSpieler[x].strafsteine))

            # Strafsteine verteilen
            if aktuelleHaelfte.has_strafsteine():
                if Config.LOG_STRAFSTEINE: print(
                    "Auf dem Stapel befinden sich {0} Strafsteine".format(aktuelleHaelfte.strafsteine))
                if Config.LOG_STRAFSTEINE: print(
                    "{0} bekommt {1} Straftsteine vom Stapel".format(rundenVerlierer, strafe))
                aktuelleHaelfte.verteile_strafsteine(rundenVerlierer, strafe)
            else:
                if Config.LOG_STRAFSTEINE: print("Auf dem Stapel befinden sich keine Strafsteine mehr.")
                if Config.LOG_STRAFSTEINE: print(
                    "{0} bekommt {1} Straftsteine von {2}".format(rundenVerlierer, strafe, rundenBester))
                verteilteSteine = rundenBester.verteile_strafsteine(rundenVerlierer, strafe)

            if gesamtErgebnis.is_schock_aus():
                aktuelleHaelfte.verlierer = rundenVerlierer
                rundenVerlierer.add_markierungsstein()
            else:
                # Gibt es einen Verlierer?
                for x in range(0, len(aktiveSpieler)):
                    spieler = aktiveSpieler[x]
                    if spieler.has_haelfte_verloren():
                        if Config.LOG_STRAFSTEINE: print(
                            "{0} hat jetzt {1} Strafsteine".format(spieler, spieler.strafsteine))
                        aktuelleHaelfte.verlierer = spieler
                        spieler.add_markierungsstein()

        # Eine Hälfte ist vorbei
        aktuellesSpiel.add_haelfte(aktuelleHaelfte)
        if Config.LOG_HAELFTEN: print()
        if Config.LOG_HAELFTEN: print(
            "Die {0}. Hälfte hat {1} verloren.".format(aktuellesSpiel.get_aktuelle_haelfte_nummer(),
                                                       aktuelleHaelfte.verlierer))
        if Config.LOG_HAELFTEN: print()

        # Verlierer muss in der nächsten Runde anfangen
        verlierer = aktiveSpieler.pop(aktiveSpieler.index(aktuelleHaelfte.verlierer))
        aktiveSpieler.insert(0, verlierer)

        # Spielsteine zurücksetzen
        for x in range(0, len(aktiveSpieler)):
            aktiveSpieler[x].erase_strafsteine()

    # Markierungssteine löschen
    for x in range(0, len(aktiveSpieler)):
        aktiveSpieler[x].erase_markierungsstein()

    if Config.LOG_SPIEL: print("=====================")
    if Config.LOG_SPIEL: print("Das {0}. Spiel ist aus".format(aktuellesSpiel.nummer))
    if Config.LOG_SPIEL: print("=====================")
    if Config.LOG_SPIEL: print()
    if Config.LOG_SPIEL: print("{0} hat verloren und muss eine Runde ausgeben!".format(aktuellesSpiel.get_verlierer()))
    if Config.LOG_SPIEL: print()
