import wiki
import plassering
import gjennomsnitt
import funksjoner

def main():
    while True:
        print("\033[38;2;234;84;159m------------------Eurovision-----------------\033[0m") 
         # 38;2 foreground
         # 234;84;159 er RGB verdiene for fargen

        print("1. For å finne tidligere resultat til et valgfritt land i Eurovision ved hjelp av Wikipedia")
        print("2. For å lage grafer for gjennomsnittlig poengsum til Sverige og Norge i Eurovision")
        print("3. Norge og Sveriges plassering???")
        print("4. For å finne gjennomsnittlig poengsum med avvik")
        print("x. Avslutt")

        print("\n")
        valg = input("\033[38;2;234;84;159mSkriv ditt valg): \033[0m")
    
        if valg.lower() == "x" or valg == "5":
            break
        elif valg == "1":
            wiki.main()  
        elif valg == "2":
            funksjoner.main()
        elif valg == "3":
            plassering.main()  
        elif valg == "4":
            gjennomsnitt.main() 
        else:
            print("Feil tegn😈 prøv igjen.")

if __name__ == "__main__":
    main()