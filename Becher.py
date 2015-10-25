# coding=utf-8

from Wuerfel import Wuerfel

class Becher(object):

    def __init__(self, spieler):
        self.wuerfelList = []
        self.spieler = spieler

    def __str__(self):
        return "Würfelbecher von {0} enthält {1} Würfel".format(self.spieler, len(self.wuerfelList))

    def entnehmeAlleWuerfel(self):
        wuerfelList = []
        for x in xrange(0,len(self.wuerfelList)):
            wuerfelList.append(self.wuerfelList.pop())
        return wuerfelList

    def befuellen(self, wuerfelList):
        for x in xrange(0,len(wuerfelList)):
            w = wuerfelList.pop();
            self.wuerfelList.append(w)
            w.setImBecher(True)

    def befuelle(self, wuerfel):
        self.wuerfelList.append(wuerfel)
        wuerfel.setImBecher(True)

    def wuerfeln(self):
        for x in xrange(0,len(self.wuerfelList)):
            self.wuerfelList[x].wuerfeln()

    def aufdecken(self):
        for x in xrange(0,len(self.wuerfelList)):
            self.wuerfelList[x].setImBecher(False)
        return self.entnehmeAlleWuerfel()

