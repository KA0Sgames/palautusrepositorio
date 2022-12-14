from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostokset_sanakirjana = {}
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 
        maara = 0

        for ostos in self.ostokset_sanakirjana.values():
            maara += ostos.lukumaara()

        return maara

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        hinta = 0

        for ostos in self.ostokset_sanakirjana.values():
            hinta += ostos.hinta()

        return hinta

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        if lisattava.nimi() not in self.ostokset_sanakirjana:
            self.ostokset_sanakirjana[lisattava.nimi()] = Ostos(lisattava)
        else:
            self.ostokset_sanakirjana[lisattava.nimi()].muuta_lukumaaraa(1)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        self.ostokset_sanakirjana[poistettava.nimi()].muuta_lukumaaraa(-1)

        if self.ostokset_sanakirjana[poistettava.nimi()].lukumaara() == 0:
            self.ostokset_sanakirjana.pop(poistettava.nimi(), None)

    def tyhjenna(self):
        # tyhjentää ostoskorin
        self.ostokset_sanakirjana = {}

    def ostokset(self):
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
        lista_ostoksista = []
        
        for ostos in self.ostokset_sanakirjana.values():
            lista_ostoksista.append(ostos)

        return lista_ostoksista