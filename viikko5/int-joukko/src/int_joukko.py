class IntJoukko:
    KAPASITEETTI = 5
    OLETUSKASVATUS = 5

    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = IntJoukko.KAPASITEETTI
        self.kasvatuskoko = IntJoukko.OLETUSKASVATUS

        if kapasiteetti is not None and self.is_valid_integer(kapasiteetti):
            self.kapasiteetti = kapasiteetti
        if kasvatuskoko is not None and self.is_valid_integer(kasvatuskoko):
            self.kasvatuskoko = kasvatuskoko

        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def is_valid_integer(self, number):
        if not isinstance(number, int) or number < 0:
            raise Exception("Kapasiteetin ja kasvatuskoon tulee olla positiivisa kokonaislukuja.")
        else:
            return True

    def kuuluu(self, n):
        if n in self.ljono:
            return True
        else:
            return False

    def lista_on_taynna(self):
        if self.alkioiden_lkm % len(self.ljono) == 0:
            return True
        else:
            return False
    
    def kasvata_listaa(self):
        self.ljono = self.ljono + self._luo_lista(self.kasvatuskoko)

    def lisaa(self, n):
        if not self.kuuluu(n):

            if self.lista_on_taynna():
                self.kasvata_listaa()

            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            return True

        return False

    def poista(self, n):
        if self.kuuluu(n):
            self.ljono.remove(n)
            self.ljono.append(0)
            self.alkioiden_lkm -= 1
            return True
        return False

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]
    
    # Tämän voisi poistaa kokonaan, tai nimi on vähän kehno ja sen voisi vaihtaa, mutta sitä käytetään testeissä, joten en muuttanut.
    def mahtavuus(self):
        return self.alkioiden_lkm

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.ljono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.ljono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
