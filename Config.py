# coding=utf-8

from peewee import *

from playhouse.postgres_ext import *

class Config(object):

    PSQL_DB = PostgresqlExtDatabase(
        'schock_db',
        user='schock_owner',
        password='schock',
        host='127.0.0.1',
        #fields={'haelfte': 'haelfte[]'}
    )

    # ca. 10  s für 1000 Spiele
    # ca.  1  s für 100  Spiele
    # ca.  0.1s für 10   Spiele
    ANZAHL_SPIELE = 1000
    ANZAHL_SPIELER = 3

    MAX_ANZAHL_WUERFE = 3
    MAX_ANZAHL_HAELFTEN = 3 #Ja 2 Hälften + Finale
    MAX_STRAFSTEINE = 13 #13, 15 oder 17
    WUERFELSEITEN = 6

    # Logging-Steuerung
    LOG_WUERFE = False
    LOG_ZUEGE = False
    LOG_RUNDEN = False
    LOG_STRAFSTEINE = False
    LOG_HAELFTEN = False
    LOG_SPIEL = True

    RANGFOLGE = [ # Schock Würfe
                 [1,1,1], #0
                 [6,1,1], #1
                 [5,1,1], #2
                 [4,1,1], #3
                 [3,1,1], #4
                 [2,1,1], #5
                 # Generäle
                 [6,6,6], #6
                 [5,5,5],
                 [4,4,4],
                 [3,3,3],
                 [2,2,2], #10
                 # Straßen
                 [6,5,4], #11
                 [5,4,3],
                 [3,2,1], #13
                 # Zahlen 6er
                 [6,6,5], #14
                 [6,6,4],
                 [6,6,3],
                 [6,6,2],
                 [6,6,1],
                 [6,5,5],
                 [6,5,4],
                 [6,5,3],
                 [6,5,2],
                 [6,5,1],
                 [6,4,4],
                 [6,4,3],
                 [6,4,2],
                 [6,4,1],
                 [6,3,3],
                 [6,3,2],
                 [6,3,1],
                 [6,2,2],
                 [6,2,1], #32
                 # Zahlen 5er
                 [5,5,4], #33
                 [5,5,3],
                 [5,5,2],
                 [5,5,1],
                 [5,4,4],
                 [5,4,3],
                 [5,4,2],
                 [5,4,1],
                 [5,3,3],
                 [5,3,2],
                 [5,3,1],
                 [5,2,2],
                 [5,2,1], #45
                 # Zahlen 4er
                 [4,4,3], #46
                 [4,4,2],
                 [4,4,1],
                 [4,3,3],
                 [4,3,2],
                 [4,3,1],
                 [4,2,2],
                 [4,2,1], #53
                 # Zahlen 3er
                 [3,3,2], #54
                 [3,3,1],
                 [3,2,2],
                 [3,2,1], #57
                 # Zahlen 2er
                 [2,2,1] #58
                ]