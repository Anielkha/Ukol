#cast_1
import requests

ico = input("Zadejte IČO subjektu: ")
url = f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    obchodni_jmeno = data.get('obchodniJmeno', 'N/A')
    adresa = data.get('sidlo', {}).get('textovaAdresa', 'N/A')
    print(f"{obchodni_jmeno}\n{adresa}")
else:
    print("Nepodařilo se získat data. Zkontrolujte zadané IČO.")

#cast_2
import requests
nazev_subjektu = input("Zadejte název subjektu nebo část názvu: ")
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}
data = f'{{"obchodniJmeno": "{nazev_subjektu}"}}'
url = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat"
response = requests.post(url, headers=headers, data=data)
if response.status_code == 200:
    vysledky = response.json()
    pocet_celkem = vysledky.get("pocetCelkem", 0)
    print(f"Nalezeno subjektů: {pocet_celkem}")

    subjekty = vysledky.get("ekonomickeSubjekty", [])
    for subjekt in subjekty:
        obchodni_jmeno = subjekt.get("obchodniJmeno", "Neznámé jméno")
        ico = subjekt.get("ico", "Neznámé IČO")
        print(f"{obchodni_jmeno}, {ico}")
else:
    print("Chyba při komunikaci s API. Zkuste to znovu později.")

