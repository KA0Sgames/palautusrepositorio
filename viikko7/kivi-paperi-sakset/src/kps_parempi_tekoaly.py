from kivi_paperi_sakset import KiviPaperiSakset

class KPSParempiTekoaly(KiviPaperiSakset):
    # En keksinyt hyvää tapaa poistaa copy-paste tästä metodista, joka on lähes identtinen KPSTekoaly luokan metodin kanssa
    # Ehkä yksi tapa olisi lisätä perintään uusi välikerros jossa näiden yhteinen toteutus tehdään
    def _toisen_siirto(self):
        siirto = self._tekoaly.anna_siirto()

        print("Toisen pelaajan siirto:", siirto)
        self._tekoaly.aseta_siirto(self.ekan_siirto)

        return siirto