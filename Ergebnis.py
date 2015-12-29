# coding=utf-8

class Ergebnis(object):
    RANGFOLGE = [  # Schock Würfe
        [1, 1, 1],  # 0
        [6, 1, 1],  # 1
        [5, 1, 1],  # 2
        [4, 1, 1],  # 3
        [3, 1, 1],  # 4
        [2, 1, 1],  # 5
        # Generäle
        [6, 6, 6],  # 6
        [5, 5, 5],
        [4, 4, 4],
        [3, 3, 3],
        [2, 2, 2],  # 10
        # Straßen
        [6, 5, 4],  # 11
        [5, 4, 3],
        [3, 2, 1],  # 13
        # Zahlen 6er
        [6, 6, 5],  # 14
        [6, 6, 4],
        [6, 6, 3],
        [6, 6, 2],
        [6, 6, 1],
        [6, 5, 5],
        [6, 5, 4],
        [6, 5, 3],
        [6, 5, 2],
        [6, 5, 1],
        [6, 4, 4],
        [6, 4, 3],
        [6, 4, 2],
        [6, 4, 1],
        [6, 3, 3],
        [6, 3, 2],
        [6, 3, 1],
        [6, 2, 2],
        [6, 2, 1],  # 32
        # Zahlen 5er
        [5, 5, 4],  # 33
        [5, 5, 3],
        [5, 5, 2],
        [5, 5, 1],
        [5, 4, 4],
        [5, 4, 3],
        [5, 4, 2],
        [5, 4, 1],
        [5, 3, 3],
        [5, 3, 2],
        [5, 3, 1],
        [5, 2, 2],
        [5, 2, 1],  # 45
        # Zahlen 4er
        [4, 4, 3],  # 46
        [4, 4, 2],
        [4, 4, 1],
        [4, 3, 3],
        [4, 3, 2],
        [4, 3, 1],
        [4, 2, 2],
        [4, 2, 1],  # 53
        # Zahlen 3er
        [3, 3, 2],  # 54
        [3, 3, 1],
        [3, 2, 2],
        [3, 2, 1],  # 57
        # Zahlen 2er
        [2, 2, 1]  # 58
    ]

    def __init__(self, augen):
        self.augen = sorted(augen, reverse=True)

    def __str__(self):
        return "[{0}]".format(",".join(str(x) for x in self.augen))

    def is_schock(self):
        einsen = [i for i in self.augen if i == 1]
        return len(einsen) >= 2

    def is_schock_aus(self):
        einsen = [i for i in self.augen if i == 1]
        return len(einsen) >= 3

    def get_strafstein_wertigkeit(self):

        rangfolge_index = Ergebnis.RANGFOLGE.index(self.augen)
        for x in range(0, len(Ergebnis.RANGFOLGE)):
            if self.augen == Ergebnis.RANGFOLGE[x]:
                rangfolge_index = x
                break

        # print "Gewinner-Ergebnis: {0} ".format(self)
        # print "Index: {0} ".format(rangfolge_index)

        if rangfolge_index == 0:
            # Schock-Aus
            return 13
        elif rangfolge_index == 1:
            return 6
        elif rangfolge_index == 2:
            return 5
        elif rangfolge_index == 3:
            return 4
        elif rangfolge_index == 4:
            return 3
        elif rangfolge_index == 5:
            return 2
        elif 6 <= rangfolge_index <= 10:
            # Pushs
            return 3
        elif 11 <= rangfolge_index <= 13:
            # Straßen
            return 2
        elif rangfolge_index >= 14:
            # Zahlen
            return 1

    def __lt__(self, other):
        if type(self) != Ergebnis or type(other) != Ergebnis:
            print("EXCEPTION: Vergleichsobjekt ist kein 'Ergebnis'")

        lt = Ergebnis.RANGFOLGE.index(self.augen) < Ergebnis.RANGFOLGE.index(other.augen)
        return lt

    '''
    def __le__(self, other):
        return Ergebnis.RANGFOLGE.index(self) <= Ergebnis.RANGFOLGE.index(other)

    
    def __eq__(self, other):
        same = True
        print(type(other[0]))
        for x in range(0,len(self.augen)):
            same = same & self.augen[x] == other[x]
        return same


    def __ne__(self, other):
        return Ergebnis.RANGFOLGE.index(self) != Ergebnis.RANGFOLGE.index(other)

    def __gt__(self, other):
        return Ergebnis.RANGFOLGE.index(self) > Ergebnis.RANGFOLGE.index(other)

    def __ge__(self, other):
        return Ergebnis.RANGFOLGE.index(self) >= Ergebnis.RANGFOLGE.index(other)
    '''
