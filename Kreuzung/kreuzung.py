from ampel import Ampel

class Kreuzung(object):
    def __init__(self):
        self._ampeln = {}
        self._ampeln[1] = Ampel("rot")
        self._ampeln[2] = Ampel("rot")
        self._ampeln[3] = Ampel("rot")
        self._ampeln[4] = Ampel("rot")
        
        self._turn13 = True

    def getAmpel(self, number: int) -> Ampel:
        if number <= 0 or number > 4:
            return None
        return self._ampeln[number]

    def printLampen(self) -> print:
        for i in range(len(self._ampeln)):
            print(f"Ampel {i+1}: {self._ampeln[i+1].getLampen()}")
        print("-----------------------------")

    def getLampen(self) -> dict:
        lampen = {}
        lampen[1] = self._ampeln[1].getLampen()
        lampen[2] = self._ampeln[2].getLampen()
        lampen[3] = self._ampeln[3].getLampen()
        lampen[4] = self._ampeln[4].getLampen()
        return lampen

    def getZustand(self) -> dict:
        zustaende = {}
        zustaende[1] = self._ampeln[1].zustand
        zustaende[2] = self._ampeln[2].zustand
        zustaende[3] = self._ampeln[3].zustand
        zustaende[4] = self._ampeln[4].zustand
        return zustaende
        

    def schalten(self):
        repairAmpeln()
        if self._turn13:
            self._ampeln[1].schalten()
            self._ampeln[3].schalten()
            if self._ampeln[1].getLampen() == (True, False, False):
                self._turn13 = False
        else:
            self._ampeln[2].schalten()
            self._ampeln[4].schalten()
            if self._ampeln[2].getLampen() == (True, False, False):
                self._turn13 = True

    def repairAmpeln(self):
        if (self._ampeln[1].zustand != self._ampeln[3].zustand or self._ampeln[2].zustand != self._ampeln[4].zustand):
            for a in self._ampeln:
                a.setZustand("rot")
            
