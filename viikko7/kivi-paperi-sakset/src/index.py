from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly
from tuomari import oletus_tuomari
from tekoaly import oletus_tekoaly

def print_pelin_loppu():
    print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

def main():
    tuomari = oletus_tuomari
    normaali_tekoaly = oletus_tekoaly

    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        if vastaus.endswith("a"):
            print_pelin_loppu()

            kaksinpeli = KPSPelaajaVsPelaaja(tuomari, None)
            kaksinpeli.pelaa()
        elif vastaus.endswith("b"):
            print_pelin_loppu()

            yksinpeli = KPSTekoaly(tuomari, normaali_tekoaly)
            yksinpeli.pelaa()
        elif vastaus.endswith("c"):
            print_pelin_loppu()

            haastava_yksinpeli = KPSParempiTekoaly()
            haastava_yksinpeli.pelaa()
        else:
            break

if __name__ == "__main__":
    main()
