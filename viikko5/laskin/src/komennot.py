class Summa:
    def __init__(self, sovelluslogiikka, syotteenlukija):
        self.logiikka = sovelluslogiikka
        self.lukija = syotteenlukija

    def suorita(self):
        arvo = int(self.lukija())
        self.logiikka.plus(arvo)

class Erotus:
    def __init__(self, sovelluslogiikka, syotteenlukija):
        self.logiikka = sovelluslogiikka
        self.lukija = syotteenlukija

    def suorita(self):
        arvo = int(self.lukija())
        self.logiikka.miinus(arvo)

class Nollaus:
    def __init__(self, sovelluslogiikka):
        self.logiikka = sovelluslogiikka

    def suorita(self):
        self.logiikka.nollaa()

class Kumoa:
    def __init__(self, sovelluslogiikka, syotteenlukija):
        self.logiikka = sovelluslogiikka
        self.lukija = syotteenlukija

    def suorita(self):
        pass