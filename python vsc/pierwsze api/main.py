from fastapi import FastAPI
import requests

app = FastAPI()

wspolrzedne_miast = {
    "Warszawa": {"lat": 52.23, "lon": 21.01},
    "Krakow": {"lat": 50.06, "lon": 19.94},
    "Myszkow": {"lat": 50.57, "lon": 19.32},
    "Gdansk": {"lat": 54.35, "lon": 18.64}
}

@app.get("/")
def powitanie():
    return {"wiadomosc": "Witaj w API Pogodowym Inżyniera!"}

# Endpoint do pobierania pogody dla danego miasta
@app.get("/pogoda")
def podaj_pogode(miasto: str):
    # Sprawdzenie miasta
    if miasto not in wspolrzedne_miast:
        return {"blad": f"Nie znamy miasta: {miasto}. Dostępne miasta to: Warszawa, Krakow, Myszkow, Gdansk."}
    
    # Wyciagniecie wspolrzednych dla miasta
    lat = wspolrzedne_miast[miasto]["lat"]
    lon = wspolrzedne_miast[miasto]["lon"]
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    
    # Zapytanie do serwera Open-Meteo
    odpowiedz = requests.get(url)
    
    # Zwrot danych po pozytywnym zapytaniu
    if odpowiedz.status_code == 200:
        dane_pogodowe = odpowiedz.json()
        temperatura = dane_pogodowe["current_weather"]["temperature"]
        
        # Zwracanie danych pogodowych w formacie JSON
        return {
            "miasto": miasto,
            "temperatura": temperatura,
            "jednostka": "°C",
            "status": "Sukces"
        }
    else:
        return {"blad": "Problem z zewnętrznym dostawcą pogody."}