from fastapi import APIRouter
import random

# Importujemy rzeczy z wlasnych plikow
from schemas import PaczkaZakladu, PaczkaDoladowania
import state

# Tworzymy router (zamiast app = FastAPI())
router = APIRouter()

@router.get("/konto")
def sprawdz_konto():
    return {
        "aktualne_saldo": state.saldo_gracza,
        "rozegrane_gry": len(state.historia_gier),
        "historia": state.historia_gier
    }

@router.post("/zagraj")
def zagraj_w_kasynie(zaklad: PaczkaZakladu):
    # Używamy state.saldo_gracza, nie ma juz zmiennych globalnych
    if zaklad.stawka > state.saldo_gracza:
        return {"blad": "Nie masz wystarczających środków!", "twoje_saldo": state.saldo_gracza}
    if zaklad.stawka <= 0:
        return {"blad": "Stawka musi być większa niż 0!"}
        
    state.saldo_gracza -= zaklad.stawka
    
    if zaklad.poziom == 1:
        wylosowana = random.randint(1, 3)
    elif zaklad.poziom == 2:
        wylosowana = random.randint(1, 10)
    else:
        state.saldo_gracza += zaklad.stawka 
        return {"blad": "Nieznany poziom! Wybierz 1 lub 2."}
        
    if zaklad.typowanie == wylosowana:
        wygrana = zaklad.stawka * state.mnozniki[zaklad.poziom]
        state.saldo_gracza += wygrana
        wynik = "Wygrałeś!"
        state.historia_gier.append(f"Wygrana: {wygrana} zł (Poziom: {zaklad.poziom})")
    else:
        wynik = "Przegrałeś!"
        state.historia_gier.append(f"Przegrana: {zaklad.stawka} zł (Poziom: {zaklad.poziom})")
        
    return {
        "wynik_gry": wynik,
        "wylosowana_liczba": wylosowana,
        "twoje_typowanie": zaklad.typowanie,
        "nowe_saldo": state.saldo_gracza
    }

@router.post("/doladuj")
def doladuj_konto(doladowanie: PaczkaDoladowania):
    state.saldo_gracza += doladowanie.kwota
    return {"wiadomosc": "Konto zasilone!", "nowe_saldo": state.saldo_gracza}