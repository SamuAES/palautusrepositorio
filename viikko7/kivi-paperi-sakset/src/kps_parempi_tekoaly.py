from tekoaly_parannettu import TekoalyParannettu
from kps_perus import KPSPerus

class KPSParempiTekoaly(KPSPerus):
    def __init__(self):
        super().__init__()
        self.tekoaly = TekoalyParannettu(10)

    def _toisen_siirto(self, toisen_siirto):
        siirto = self.tekoaly.anna_siirto()
        self.tekoaly.aseta_siirto(toisen_siirto)
        print(f"Tietokone valitsi: {siirto}")
        return siirto
