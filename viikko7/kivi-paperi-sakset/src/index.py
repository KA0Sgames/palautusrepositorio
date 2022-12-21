from kps_tehdas import KPSTehdas

VASTAUKSEN_VIIMEINEN_MERKKI = -1

def print_pelin_loppu():
    print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        if not(vastaus.endswith("a") or vastaus.endswith("b") or vastaus.endswith("c")):
            break
        
        print_pelin_loppu()

        peli = KPSTehdas.luo_peli(vastaus[VASTAUKSEN_VIIMEINEN_MERKKI])
        peli.pelaa()

if __name__ == "__main__":
    main()
