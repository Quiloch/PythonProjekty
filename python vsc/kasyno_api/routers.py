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

'''
@router.post("/zagraj")
def zagraj_w_kasynie(zaklad: schemas.PaczkaZakladu, db: Session = Depends(get_db)):
    #szukanie gracza w bazie
    gracz = crud.pobierz_gracza(db, gracz_id=zaklad.gracz_id)
    if not gracz:
        raise HTTPException(status_code=404, detail="Nie znaleziono takiego gracza")
    
    # Używamy state.saldo_gracza, nie ma juz zmiennych globalnych
    if zaklad.stawka > state.saldo_gracza:
        raise HTTPException(status_code=400, detail="Nie masz wystarczająco środków na koncie!")
    if zaklad.stawka <= 0:
        raise HTTPException(status_code=400, detail="Stawka musi być większa niż 0!")        
    mnozniki = {1: 2, 2: 5} #mnozniki dla poziomow, mozna tez trzymac w bazie danych
    if zaklad.poziom == 1:
        wylosowana = random.randint(1, 3)
    else:
        wylosowana = random.randint(1, 10)
    
    if zaklad.typowanie == wylosowana:
        wygrana_kwota = (zaklad.stawka * mnozniki[zaklad.poziom]) #obliczenie wygranej na podstawie stawki i mnoznika
        zmiana_salda = wygrana_kwota
        wynik = "Wygrałeś!"
    else:
        zmiana_salda -= zaklad.stawka #przegrana, odejmujemy stawke od salda
        wynik = "Przegrałeś!"

    zaktualizowany_gracz = crud.zmien_saldo(db, gracz_id=zaklad.gracz_id, kwota=zmiana_salda)
        
    return {
        "wynik_gry": wynik,
        "wylosowana_liczba": wylosowana,
        "twoje_typowanie": zaklad.typowanie,
        "nowe_saldo": zaktualizowany_gracz.saldo
    }


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
