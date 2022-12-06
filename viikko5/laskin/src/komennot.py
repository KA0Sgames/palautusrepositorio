class Summa:
    def __init__(self, sovelluslogiikka, syotteenlukija):
        self.logiikka = sovelluslogiikka
        self.lukija = syotteenlukija

    def suorita(self):
        self.ennen_operaatiota = self.logiikka.hae_arvo()
        self.arvo = int(self.lukija())
        self.logiikka.plus(self.arvo)

    def kumoa(self):
        self.logiikka.aseta_arvo(self.arvo)

class Erotus:
    def __init__(self, sovelluslogiikka, syotteenlukija):
        self.logiikka = sovelluslogiikka
        self.lukija = syotteenlukija

    def suorita(self):
        self.ennen_operaatiota = self.logiikka.hae_arvo()
        arvo = int(self.lukija())
        self.logiikka.miinus(arvo)

    def kumoa(self):
        self.logiikka.aseta_arvo(self.ennen_operaatiota)

class Nollaus:
    def __init__(self, sovelluslogiikka):
        self.logiikka = sovelluslogiikka

    def suorita(self):
        self.ennen_operaatiota = self.logiikka.hae_arvo()
        self.logiikka.nollaa()

    def kumoa(self):
        self.logiikka.aseta_arvo(self.ennen_operaatiota)

class Kumoa:
    def __init__(self, sovelluslogiikka):
        self.logiikka = sovelluslogiikka
        self.viimeinen_komento = None

    def suorita(self):
        self.viimeinen_komento.kumoa()

    def aseta_edellinen_komento(self, komento):
        self.viimeinen_komento = komento