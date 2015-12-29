# coding=utf-8

import random
from Config import Config


class Wuerfel(object):
    def __init__(self):
        self.augenzahl = random.randint(1, Config.WUERFELSEITEN)
        self.imBecher = False

    def __str__(self):
        return str(self.augenzahl)

    def wuerfeln(self):
        self.augenzahl = random.randint(1, Config.WUERFELSEITEN)

    def set_im_becher(self, imbecher):
        self.imBecher = imbecher

    def is_im_becher(self):
        return self.imBecher

    def __lt__(self, other):
        if type(self) != Wuerfel or type(other) != Wuerfel:
            print("EXCEPTION: Vergleichsobjekt ist kein 'Ergebnis'")
        return self.augenzahl < other.augenzahl
