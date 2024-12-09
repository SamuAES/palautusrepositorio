from kps import KiviPaperiSakset

def main():

    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        if vastaus == "a":
            KiviPaperiSakset.pelaaja_vs_pelaaja()
        elif vastaus == "b":
            KiviPaperiSakset.pelaaja_vs_tekoaly()
        elif vastaus == "c":
            KiviPaperiSakset.pelaaja_vs_parempi_tekoaly()
        else:
            break


if __name__ == "__main__":
    main()
