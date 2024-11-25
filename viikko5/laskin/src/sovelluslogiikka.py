class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._edellinen_arvo = 0

    def miinus(self, operandi):
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo
    
    def aseta_edellinen_arvo(self, luku):
        self._edellinen_arvo = luku

    def palauta_edellinen_arvo(self):
        self._arvo = self._edellinen_arvo

class BinaariOperaatio:
    def __init__(self, sovelluslogiikka:Sovelluslogiikka, lue_syote:callable):
        self.sovelluslogiikka = sovelluslogiikka
        self.luku = lue_syote
    
class Summa(BinaariOperaatio):
    def __init__(self, sovelluslogiikka, lue_syote):
        super().__init__(sovelluslogiikka, lue_syote)

    def suorita(self):
        edellinen_arvo = self.sovelluslogiikka.arvo()
        try:
            self.sovelluslogiikka.plus(self.luku())
            self.sovelluslogiikka.aseta_edellinen_arvo(edellinen_arvo)
        except Exception:
            pass

class Erotus(BinaariOperaatio):
    def __init__(self, sovelluslogiikka, lue_syote):
        super().__init__(sovelluslogiikka, lue_syote)
    
    def suorita(self):
        edellinen_arvo = self.sovelluslogiikka.arvo()
        try:
            self.sovelluslogiikka.miinus(self.luku())
            self.sovelluslogiikka.aseta_edellinen_arvo(edellinen_arvo)
        except Exception:
            pass

class Nollaus:
    def __init__(self, sovelluslogiikka:Sovelluslogiikka):
        self.sovelluslogiikka = sovelluslogiikka
    
    def suorita(self):
        edellinen_arvo = self.sovelluslogiikka.arvo()
        try:
            self.sovelluslogiikka.aseta_arvo(0)
            self.sovelluslogiikka.aseta_edellinen_arvo(edellinen_arvo)
        except Exception:
            pass

class Kumoa:
    def __init__(self, sovelluslogiikka:Sovelluslogiikka):
        self.sovelluslogiikka = sovelluslogiikka

    def suorita(self):
        self.sovelluslogiikka.palauta_edellinen_arvo()