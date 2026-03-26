import requests

url = "https://api.nbp.pl/api/exchangerates/rates/a/usd/?format=json"

odpowiedz = requests.get(url)

if odpowiedz.status_code == 200:
    dane = odpowiedz.json()
    
    print(f"Aktualny kurs USD wynosi: {dane['rates'][0]['mid']}")