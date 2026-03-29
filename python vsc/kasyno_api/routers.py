from fastapi import APIRouter, Depends, HTTPException
import random
from sqlalchemy.orm import Session
from database import SessionLocal
import crud, schemas


# Tworzymy router (zamiast app = FastAPI())
router = APIRouter()

#stworzenie logiki otwierania i zamykania sesji bazy danych
def get_db():
    db = SessionLocal()
    try:
        yield db #zatrzymanie sie kodu w tym miejscu, przekazanie bazy danych do endpoitu
    finally:
        db.close() #zamkniecie sesji, gdy endpoint skonczy prace, polaczenie ZAWSZE jest zamkniete


#endpoint do rejestracji gracza, przyjmuje dane z requesta, tworzy gracza w bazie danych i zwraca informacje o nim
@router.post("/rejestracja", response_model=schemas.GraczResponse)
def zarejestruj_gracza(gracz: schemas.GraczCreate, db: Session = Depends(get_db)):
    utworzony_gracz = crud.stworz_gracza(db=db, gracz=gracz)
    return utworzony_gracz


#endpoint do sprawdzania stanu konta gracza, przyjmuje ID gracza jako parametr, pobiera informacje o graczu z bazy danych i zwraca je
@router.get("/konto/{gracz_id}", response_model=schemas.GraczResponse)
def sprawdz_konto(gracz_id: int, db: Session = Depends(get_db)):
    gracz = crud.pobierz_gracza(db, gracz_id=gracz_id)

    #zabezpieczenie przed brakiem gracza o podanym ID
    if gracz is None:
        raise HTTPException(status_code=404, detail="Nie znaleziono takiego gracza")
    
    return gracz


@router.get("/test_bazy")
def test_polaczenia(db: Session = Depends(get_db)):
    #depends "mowi" do FastApi ze przed wywolaniem tej funkcji, musi wywolac get_db() i przekazac wynik jako argument db
    return {"status": "Połączenie z bazą działa", "typ_sesji": str(type(db))}


'''@router.get("/konto")
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

'''
@router.post("/doladuj", response_model=schemas.GraczResponse)
def doladuj_konto(doladowanie: schemas.PaczkaDoladowania, db: Session = Depends(get_db)):
    #sprawdzenie czy gracz istnieje
    gracz = crud.pobierz_gracza(db, gracz_id=doladowanie.gracz_id)
    if not gracz:
        raise HTTPException(status_code=404, detail="Nie znaleziono takiego gracza")
    
    #sprawdzenie czy kwota doladowania jest dodatnia
    if doladowanie.kwota <= 0:
        raise HTTPException(status_code=400, detail="Kwota doładowania musi być większa niż 0")
    
    #aktualizacja salda gracza w bazie danych

    zaktualizowany_gracz = crud.dodaj_do_salda(db, gracz_id=doladowanie.gracz_id, kwota=doladowanie.kwota)
    return zaktualizowany_gracz
