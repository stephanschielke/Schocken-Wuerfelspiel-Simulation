class Ergebnis(object):

    def __init__(self, augen):
        self.augen = sorted(augen, reverse=True)

    def __str__(self):

        return "[{0}]".format(",".join(str(x) for x in self.augen))
