from kivi_paperi_sakset import KiviPaperiSakset

class KPSTekoaly(KiviPaperiSakset):
    def _toisen_siirto(self):
        siirto = self._tekoaly.anna_siirto()
        
        print("Toisen pelaajan siirto:", siirto)

        return siirto