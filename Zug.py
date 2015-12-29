# coding=utf-8


class Zug(object):
    def __init__(self, spieler):
        self.spieler = spieler
        self.wuerfe = []
        self.endergebnis = None

    def __str__(self):
        return "{0} mit Endergebnis {1}".format(self.spieler, self.endergebnis)

    def get_last_wurf(self):
        return self.wuerfe[len(self.wuerfe) - 1]

    def add_wurf(self, wurf):
        self.wuerfe.append(wurf)

    def aktueller_wurf(self):
        return len(self.wuerfe) + 1

    def __lt__(self, other):
        return self.endergebnis < other.endergebnis


'''
    def __le__(self, other):
        return self.endergebnis <= other.endergebnis

    def __eq__(self, other):
        if other == None :
            return False
        return self.endergebnis == other.endergebnis

    def __ne__(self, other):
        if other == None :
            return True

        return self.endergebnis != other.endergebnis

    def __gt__(self, other):
        return self.endergebnis > other.endergebnis

    def __ge__(self, other):
        return self.endergebnis >= other.endergebnis
        '''
