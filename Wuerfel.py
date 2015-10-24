# coding=utf-8

import random

class Wuerfel(object):

    def __init__(self):
        self.augenzahl = random.randint(1,6)
        self.imBecher = False

    def __str__(self):
        return str(self.augenzahl)

    def wuerfeln(self):
        self.augenzahl = random.randint(1,6)

    def setImBecher(self, imBecher):
        self.imBecher = imBecher

    def isImBecher(self):
        return self.imBecher

    def getAugenzahl(self):
        return self.augenzahl

