from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

# Nasza "baza danych" w pamięci RAM serwera
saldo_gracza = 100
historia_gier = []
mnozniki = {1: 2, 2: 5}

# 1. Definiujemy, jakiej paczki danych (JSON) oczekujemy od klienta
class PaczkaZakladu(BaseModel):
    poziom: int      # 1 (łatwy) lub 2 (trudny)
    stawka: int      # Ile pieniędzy stawia
    typowanie: int   # Jaką liczbę obstawia gracz

# 2. Endpoint do sprawdzania stanu konta (Metoda GET - tylko odczyt)
@app.get("/konto")
def sprawdz_konto():
    return {
        "aktualne_saldo": saldo_gracza,
        "rozegrane_gry": len(historia_gier),
        "historia": historia_gier
    }

class PaczkaDoladowania(BaseModel):
    kwota: int

# Endpoint do doladowania konta (klient przesyla kwote doladowania -> metoda POST)
@app.post("/doladuj")
def doladuj_konto(doladowanie: PaczkaDoladowania):
    global saldo_gracza
    saldo_gracza += doladowanie.kwota
    return {"wiadomosc": "Konto zasilone!", "nowe_saldo": saldo_gracza}

# 3. Endpoint do grania (Metoda POST - klient przysyła nam dane!)
@app.post("/zagraj")
def zagraj_w_kasynie(zaklad: PaczkaZakladu):
    global saldo_gracza # Informujemy Pythona, że chcemy modyfikować zmienną globalną
    
    # Krok 1: Walidacja, czy gracza w ogóle stać na grę
    if zaklad.stawka > saldo_gracza:
        return {"blad": "Nie masz wystarczających środków!", "twoje_saldo": saldo_gracza}
    if zaklad.stawka <= 0:
        return {"blad": "Stawka musi być większa niż 0!"}
        
    # Krok 2: Pobieramy pieniądze z konta
    saldo_gracza -= zaklad.stawka
    
    # Krok 3: Logika losowania
    if zaklad.poziom == 1:
        wylosowana = random.randint(1, 3)
    elif zaklad.poziom == 2:
        wylosowana = random.randint(1, 10)
    else:
        # Zwracamy graczowi stawkę, bo podał zły poziom
        saldo_gracza += zaklad.stawka 
        return {"blad": "Nieznany poziom! Wybierz 1 lub 2."}
        
    # Krok 4: Sprawdzamy wygraną
    if zaklad.typowanie == wylosowana:
        wygrana = zaklad.stawka * mnozniki[zaklad.poziom]
        saldo_gracza += wygrana
        wynik = "Wygrałeś!"
        historia_gier.append(f"Wygrana: {wygrana} zł (Poziom: {zaklad.poziom})")
    else:
        wygrana = 0
        wynik = "Przegrałeś!"
        historia_gier.append(f"Przegrana: {zaklad.stawka} zł (Poziom: {zaklad.poziom})")
        
    # Krok 5: Zwracamy piękny paragon (JSON) z wynikiem gry
    return {
        "wynik_gry": wynik,
        "wylosowana_liczba": wylosowana,
        "twoje_typowanie": zaklad.typowanie,
        "nowe_saldo": saldo_gracza
    }