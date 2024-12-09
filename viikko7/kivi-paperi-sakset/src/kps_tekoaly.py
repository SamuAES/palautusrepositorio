from tekoaly import Tekoaly
from kps_perus import KPSPerus

class KPSTekoaly(KPSPerus):
    def __init__(self):
        super().__init__()
        self.tekoaly = Tekoaly()

    def _toisen_siirto(self, toisen_siirto):
        siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        return siirto