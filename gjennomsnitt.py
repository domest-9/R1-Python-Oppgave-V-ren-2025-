import pandas as pd

def main():
    land = input("Velg et land du vil finne gjennomsnitt påeng for: ").lower()  # passer på så landet ender opp i lowercase, 
# ellerss funker ikke programmet siden filene er lagret i lowercase


# leser Excel filen fra directoriet datasett
# bruker {} for å sette inn variabelen land i filnavnet
    datasett = pd.read_excel(f'datasett/{land}.xlsx') 
    
    sum_land = datasett['Points'].sum()
    antall_rader_land = len(datasett)
    gjennomsnitt_land = sum_land / antall_rader_land

    print(f"Gjennomsnitt påeng for {land.capitalize()}: {gjennomsnitt_land:.2f}")
# capitalize() for å gjøre første bokstav stor igjen

if __name__ == "__main__":
    main()