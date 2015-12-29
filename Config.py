# coding=utf-8

class Config(object):
    # ca. 10  s für 1000 Spiele
    # ca.  1  s für 100  Spiele
    # ca.  0.1s für 10   Spiele
    ANZAHL_SPIELE = 100
    ANZAHL_SPIELER = 3

    MAX_ANZAHL_WUERFE = 3
    MAX_ANZAHL_HAELFTEN = 3  # Ja 2 Hälften + Finale
    MAX_STRAFSTEINE = 13  # 13, 15 oder 17
    WUERFELSEITEN = 6

    # Logging-Steuerung
    LOG_WUERFE = False
    LOG_ZUEGE = False
    LOG_RUNDEN = False
    LOG_STRAFSTEINE = False
    LOG_HAELFTEN = False
    LOG_SPIEL = True
