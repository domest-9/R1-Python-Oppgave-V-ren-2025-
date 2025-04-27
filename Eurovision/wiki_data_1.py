import requests
from bs4 import BeautifulSoup

land = input("Skriv inn et land du vil søke etter: ")
kjærne_url = f"https://no.wikipedia.org/wiki/{land}_i_Eurovision_Song_Contest"
år = input("Skriv inn et år du vil søke etter: ")

def få_land_informasjon(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

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
                        cells_text[1] if len(cells_text) > 1 else "Ikke funnet",  # Artist
                        cells_text[2] if len(cells_text) > 2 else "Ikke funnet",  # Tittel
                        cells_text[3] if len(cells_text) > 3 else "Ikke funnet",  # Språk
                        cells_text[4] if len(cells_text) > 4 else "Ikke funnet",  # Finale
                        cells_text[5] if len(cells_text) > 5 else "Ikke funnet"   # Poeng
                    ]
    return None

wiki_info = få_land_informasjon(kjærne_url)
if wiki_info:
    eurovision_data = finn_eurovision_info(wiki_info, år)
    if eurovision_data:
        print(f"\nInformasjon for {land} i Eurovision Song Contest {år}:")
        print(f"Artist: {eurovision_data[1] if len(eurovision_data) > 1 else 'Ikke funnet'}")
        print(f"Tittel: {eurovision_data[2] if len(eurovision_data) > 2 else 'Ikke funnet'}")
        print(f"Språk: {eurovision_data[3] if len(eurovision_data) > 3 else 'Ikke funnet'}")
        print(f"Finale: {eurovision_data[4] if len(eurovision_data) > 4 else 'Ikke funnet'}")
        print(f"Poeng: {eurovision_data[5] if len(eurovision_data) > 5 else 'Ikke funnet'}")
    else:
        print(f"Fant ingen informasjon for {land} i år {år}")
