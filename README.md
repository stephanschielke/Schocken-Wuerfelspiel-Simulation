# Schocken
> Das Schocken ist ein besonders im Westfälischen und im Rheinischen beliebtes Würfelspiel, das gerne in Kneipen als Trinkspiel von mindestens zwei Spielern gespielt wird. Dabei ist es üblich, dass der Verlierer eines Spiels die nächste Runde Bier bezahlt. In Hessen ist dieses Spiel auch unter dem Namen Jule, in Niedersachsen auch als Mörkeln oder Knobeln, in Schleswig-Holstein und Hamburg als Maxen und in der Städteregion Aachen als Meiern (nicht zu verwechseln mit Mäxchen) bekannt. Der Spiegel bezeichnet es als das Würfelspiel des Reviers.
[https://de.wikipedia.org/wiki/Schocken]

## Schocken Würfelspiel Simulation
Das Python-Programm ist in der Lage Schocken-Spiele zu simulieren. Es gibt derzeit noch keine Intelligenz. Die Auswahl welche Würfel zurückgelegt werden und wieviele Würfe ein Spieler macht sind zufällig.

Der erste Entwurft ist während dem Hackathon 2015 vom CCC-Aachen entstanden.

### Ziel
Ziel dieser Simulation ist es, möglichst viele Random-Spiele zu erzeugen und Gewinntaktiken zu erkennen.

### Zum Spielaufbau
Ein Spiel besteht aus 1-2 Hälften + einem Finale.

Eine Hälfte besteht aus n > 1 Runden.

Eine Runde besteht aus x (Anzahl Mitspieler) Zügen.

Ein Zug besteht aus 1-3 Würfen.

Ein Wurf hat ein Ergebnis.

### TODOs
* Zwei Sechsen zu einer Eins umdrehen, wenn danach noch ein Wurf frei ist
* "Mit-Ist-Shit"-Regel beachten
* Handwürfe > zusammengewürfelte Würfe

# Installation
## Python
> apt-get install python-pip

> pip install --upgrade pip

> pip install peewee

> apt-get install python-dev

## Datenbank
> apt-get install postgresql-contrib

> apt-get install postgresql-server-dev-all

> su postgres

> psql template1 -c 'create extension hstore;'

> psql schock_db -c 'create extension hstore;'
