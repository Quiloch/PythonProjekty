import requests

wspolrzedne_miast = {
    "Warszawa": {"lat": 52.23, "lon": 21.01},
    "Krakow": {"lat": 50.06, "lon": 19.94},
    "Myszkow": {"lat": 50.57, "lon": 19.32},
    "Gdansk": {"lat": 54.35, "lon": 18.64}
}

miasto_uzytkownika = input("Podaj nazwę miasta: ")
if miasto_uzytkownika in wspolrzedne_miast:
    lat = wspolrzedne_miast[miasto_uzytkownika]["lat"]
    lon = wspolrzedne_miast[miasto_uzytkownika]["lon"]
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    odpowiedz_serwera = requests.get(url)

    if odpowiedz_serwera.status_code == 200:
        dane_pogodowe = odpowiedz_serwera.json()
        temperatura = dane_pogodowe["current_weather"]["temperature"]
        print(f"Aktualna temperatura w {miasto_uzytkownika} wynosi {temperatura}°C.")
    else:
        print("Nie można pobrać danych pogodowych dla danego miasta.")
else:
    print("Nieznane miasto. Proszę podać jedno z następujących: Warszawa, Krakow, Myszkow, Gdansk.")