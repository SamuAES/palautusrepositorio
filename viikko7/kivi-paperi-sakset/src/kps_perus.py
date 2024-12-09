from tuomari import Tuomari

class KPSPerus:
    def pelaa(self):
        
        print(
            "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
        )

        tuomari = Tuomari()

        ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        tokan_siirto = self._toisen_siirto(ekan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
            tokan_siirto = self._toisen_siirto(ekan_siirto)

        print("Kiitos!")
        print(tuomari)

    def _onko_ok_siirto(self, siirto):
        return siirto in ["k", "p", "s"]
    
    def _toisen_siirto(self, toisen_siirto):
        siirto = input("Toisen pelaajan siirto: ") 
        return siirto