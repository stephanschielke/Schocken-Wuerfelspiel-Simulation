class Ergebnis(object):

    def __init__(self, augen):
        self.augen = sorted(augen, reverse=True)

    def __str__(self):
        return "[{0}]".format(",".join(str(x) for x in self.augen))

    def getAugen(self):
        return self.augen

    def addAugen(self, augen):
        for x in xrange(0,len(augen)):
            self.augen.append(augen[x])
