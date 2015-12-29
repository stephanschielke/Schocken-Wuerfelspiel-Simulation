# coding=utf-8


class Becher(object):
    def __init__(self, spieler):
        self.wuerfelList = []
        self.spieler = spieler

    def __str__(self):
        return "Würfelbecher von {0} enthält {1} Würfel".format(self.spieler, len(self.wuerfelList))

    def entnehme_alle_wuerfel(self):
        wuerfel_list = []
        for x in range(0, len(self.wuerfelList)):
            wuerfel_list.append(self.wuerfelList.pop())
        return wuerfel_list

    def befuellen(self, wuerfel_list):
        for x in range(0, len(wuerfel_list)):
            w = wuerfel_list.pop()
            self.wuerfelList.append(w)
            w.set_im_becher(True)

    def befuelle(self, wuerfel):
        self.wuerfelList.append(wuerfel)
        wuerfel.set_im_becher(True)

    def wuerfeln(self):
        for x in range(0, len(self.wuerfelList)):
            self.wuerfelList[x].wuerfeln()

    def aufdecken(self):
        for x in range(0, len(self.wuerfelList)):
            self.wuerfelList[x].set_im_becher(False)
        return self.entnehme_alle_wuerfel()
