import requests
from bs4 import BeautifulSoup

def få_land_informasjon(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.text
    


def finn_eurovision_info(html_content, år):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    tables = soup.find_all('table', {'class': 'wikitable'})
    
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            cells = row.find_all(['td', 'th'])
            row_text = ' '.join(cell.get_text(strip=True) for cell in cells)
            
            if år in row_text:
                cells_text = []
                for cell in cells:
                    # Remove reference tags and get clean text
                    for sup in cell.find_all('sup'):
                        sup.decompose()
                    text = cell.get_text(strip=True)
                    if text:
                        cells_text.append(text)
                
                # Ensure we have enough cells and they contain valid data
                if len(cells_text) >= 4:
                    return [
                        cells_text[0],  # År
                        cells_text[1],  # Artist
                        cells_text[2],  # Tittel
                        cells_text[3],  # Språk
                        cells_text[4],  # Finale
                        cells_text[5]   # Poeng
                    ]
    return None
def main():
    land = input("Skriv inn et land du vil søke etter på wikipedia: ")
    kjærne_url = f"https://no.wikipedia.org/wiki/{land}_i_Eurovision_Song_Contest"
    år = input("Skriv inn et år du vil søke etter: ")

    wiki_info = få_land_informasjon(kjærne_url)
    if wiki_info:
        eurovision_data = finn_eurovision_info(wiki_info, år)
        if eurovision_data:
            print(f"\nInformasjon for {land} i Eurovision Song Contest {år}:")
            print(f"Artist: {eurovision_data[1]}")
            print(f"Tittel: {eurovision_data[2]}")
            print(f"Språk: {eurovision_data[3]}")
            print(f"Finale: {eurovision_data[4]}")
            print(f"Poeng: {eurovision_data[5]}")
        else:
            print(f"Fant ingen informasjon for {land} i år {år}")

if __name__ == "__main__":
    main()
