from ampel import Ampel

class Kreuzung(object):
    def __init__(self):
        self.a1 = Ampel("rot")
        self.a2 = Ampel("gruen")
        self.a3 = Ampel("rot")
        self.a4 = Ampel("gruen")

    def getLampen(self):
        l1 = self.a1.getLampen()
        l2 = self.a2.getLampen()
        l3 = self.a3.getLampen()
        l4 = self.a4.getLampen()

        return f"Ampel 1: {l1}\nAmpel 2: {l2}\nAmpel 3: {l3}\nAmpel 4: {l4}"

    def schalten(self):
        self.a1.schalten()
        self.a2.schalten()
        self.a3.schalten()
        self.a4.schalten()