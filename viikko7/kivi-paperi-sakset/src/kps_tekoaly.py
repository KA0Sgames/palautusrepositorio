from tuomari import Tuomari
from tekoaly import Tekoaly
from kivi_paperi_sakset import KiviPaperiSakset


class KPSTekoaly(KiviPaperiSakset):
    def __init__(self, tuomari, tekoaly):
        self._tuomari = tuomari
        self._tekoaly = tekoaly

    def _toisen_siirto(self):
        siirto = self._tekoaly.anna_siirto()

        print("Toisen pelaajan siirto:", siirto)

        return siirto
