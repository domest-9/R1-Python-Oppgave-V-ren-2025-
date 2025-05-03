sverige_poeng = [88, 100, 72, 107, 170, 30, 170, 51,
                 47, 33, 185, 372, 62, 218, 365, 261, 344,
                 274, 334, 109, 438, 583, 174]

norge_poeng = [57, 3, 123, 3, 125, 36, 182,
               387, 35, 7, 191, 88, 102, 158,
               144, 331, 75, 182, 268, 16]

def main():
    def analyser(poeng, land):
        sum_poeng = 0
        antall = len(poeng)
        maks_poeng = poeng[0]
        min_poeng = poeng[0]

        # print(f"\nPoeng for {land}:")
        for p in poeng:
            # print(p)  # Skjult poengutskrift
            sum_poeng += p
            if p > maks_poeng:
                maks_poeng = p
            if p < min_poeng:
                min_poeng = p

        gjennomsnitt = sum_poeng / antall
        avvik = (maks_poeng - min_poeng) / 2

        print(f"Gjennomsnittlig poengsum for {land} er {gjennomsnitt:.2f} ± {avvik}")


    analyser(sverige_poeng, "Sverige")
    analyser(norge_poeng, "Norge")

if __name__ == "__main__":
    main()
