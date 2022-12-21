class KiviPaperiSakset:
    def __init__(self, tuomari, tekoaly):
        self._tuomari = tuomari
        self._tekoaly = tekoaly

    def pelaa(self):

        while True:
            self.ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto()

            if not (self._onko_ok_siirto(self.ekan_siirto) and self._onko_ok_siirto(tokan_siirto)):
                break

            self._tuomari.kirjaa_siirto(self.ekan_siirto, tokan_siirto)
            print(self._tuomari)

        print("Kiitos!")
        # Poistetaan tuomarin uudelleen printtaus copy-pastena, viimeisen pelatun pelin jälkeen jo printattu
        # print(self._tuomari)

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    # tämän metodin toteutus vaihtelee eri pelityypeissä
    def _toisen_siirto(self):
        # metodin oletustoteutus
        return "k"

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"