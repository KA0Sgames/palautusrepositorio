from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu
from tuomari import Tuomari

MUISTIN_KOKO = 10

class KPSTehdas:
    @staticmethod
    def luo_peli(tyyppi):
        tuomari = Tuomari.luo_tuomari()

        if tyyppi == "a":
            return KPSPelaajaVsPelaaja(tuomari, None)

        if tyyppi == "b":
            tekoaly = Tekoaly.luo_tekoaly()

            return KPSTekoaly(tuomari, tekoaly)

        if tyyppi == "c":
            tekoaly = TekoalyParannettu.luo_tekoaly(MUISTIN_KOKO)

            return KPSParempiTekoaly(tuomari, tekoaly)