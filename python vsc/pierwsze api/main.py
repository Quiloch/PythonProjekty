from fastapi import FastAPI

# 1. Tworzymy główny obiekt naszej aplikacji (naszą "restaurację")
app = FastAPI()

# 2. Tworzymy pierwszy endpoint (ścieżkę główną: "/")
# Metoda GET oznacza, że ktoś chce "pobrać" dane (jak przez przeglądarkę)
@app.get("/")
def powitanie():
    # Zwracamy zwykły słownik, FastAPI samo zrobi z tego JSON!
    return {
        "wiadomosc": "Witaj na moim pierwszym własnym serwerze!",
        "autor": "Inżynier Pythona",
        "status": "Działa perfekcyjnie"
    }

# 3. Dodajmy drugi endpoint (ścieżkę "/pogoda")
@app.get("/pogoda")
def pokaz_pogode():
    return {
        "miasto": "Warszawa",
        "temperatura": 15.2,
        "opis": "Słonecznie z przelotnym kodowaniem"
    }