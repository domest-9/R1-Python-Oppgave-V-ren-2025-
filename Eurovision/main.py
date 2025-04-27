print("1. For å finne tidligere resultat til et valgfritt land i Eurovision")
print("2. For å lage grafer for gjennomsnittlig poengsum til Sverige og Norge i Eurovision")
valg = int(input("Skriv (1 eller 2): "))

if valg == 1:
    import wiki_data_1
elif valg == 2:
    import grafer_for_gjennomsnitt_n_s
else:
    print("Feil nummer, prøv igjen.")
