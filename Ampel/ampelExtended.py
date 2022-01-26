from ampel import Ampel

class AmpelExtended(object):
    def __init__(self, anfangszustand):
        self.tageszeit = "tag"
        self.ampel = Ampel(anfangszustand)

    def tageszeitWechsel(self):
        if self.tageszeit == 'tag':
            self.tageszeit = 'nacht'
        elif self.tageszeit == 'nacht':
            self.tageszeit = 'tag'

    def schalten(self):
        if self.tageszeit == 'nacht':
            if self.ampel.zustand == 'aus':
                self.ampel.zustand = 'gelb'
            else:
                self.ampel.zustand = 'aus'
        else:
            self.ampel.schalten()
                