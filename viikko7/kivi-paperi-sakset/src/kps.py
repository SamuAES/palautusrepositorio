from kps_perus import KPSPerus
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

class KiviPaperiSakset:
    @staticmethod
    def pelaaja_vs_pelaaja():
        KPSPerus().pelaa()
    
    @staticmethod
    def pelaaja_vs_tekoaly():
        KPSTekoaly().pelaa()
    
    @staticmethod
    def pelaaja_vs_parempi_tekoaly():
        KPSParempiTekoaly().pelaa()