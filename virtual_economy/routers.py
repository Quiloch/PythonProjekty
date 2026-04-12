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


#endpoint do rejestracji uzytkownika, przyjmuje dane z requesta, tworzy uzytkownika w bazie danych i zwraca informacje o nim
@router.post("/rejestracja", response_model=schemas.UzytkownikResponse)
def zarejestruj_uzytkownika(uzytkownik: schemas.UzytkownikCreate, db: Session = Depends(get_db)):
    utworzony_uzytkownik = crud.stworz_uzytkownika(db=db, uzytkownik=uzytkownik)
    return utworzony_uzytkownik


#endpoint do sprawdzania stanu konta uzytkownika, przyjmuje ID uzytkownika jako parametr, pobiera informacje o uzytkowniku z bazy danych i zwraca je
@router.get("/konto/{uzytkownik_id}", response_model=schemas.UzytkownikResponse)
def sprawdz_konto(uzytkownik_id: int, db: Session = Depends(get_db)):
    uzytkownik = crud.pobierz_uzytkownika(db, uzytkownik_id=uzytkownik_id)

    #zabezpieczenie przed brakiem uzytkownika o podanym ID
    if uzytkownik is None:
        raise HTTPException(status_code=404, detail="Nie znaleziono takiego uzytkownika")
    
    return uzytkownik


@router.get("/test_bazy")
def test_polaczenia(db: Session = Depends(get_db)):
    #depends "mowi" do FastApi ze przed wywolaniem tej funkcji, musi wywolac get_db() i przekazac wynik jako argument db
    return {"status": "Połączenie z bazą działa", "typ_sesji": str(type(db))}


@router.post("/inwestuj")
def wykonaj_transakcje(inwestycja: schemas.PaczkaInwestycji, db: Session = Depends(get_db)):
    #szukanie uzytkownika w bazie
    uzytkownik = crud.pobierz_uzytkownika(db, uzytkownik_id=inwestycja.uzytkownik_id)
    if not uzytkownik:
        raise HTTPException(status_code=404, detail="Nie znaleziono takiego uzytkownika")
    
    if inwestycja.kwota > uzytkownik.saldo:
        raise HTTPException(status_code=400, detail="Nie masz wystarczająco środków na koncie!")
    if inwestycja.kwota <= 0:
        raise HTTPException(status_code=400, detail="Kwota musi być większa niż 0!") 
           
    mnozniki = {1: 2, 2: 5} #mnozniki dla poziomow ryzyka; 1- niskie, 2-wysokie
    if inwestycja.poziom_ryzyka not in mnozniki:
        raise HTTPException(status_code=400, detail="Nieprawidłowy poziom ryzyka!")
    
    if inwestycja.poziom_ryzyka == 1:
        wylosowana = random.randint(1, 3)
    else:
        wylosowana = random.randint(1, 10)
    
    # rozliczenie
    if inwestycja.prognoza == wylosowana:
        wygrana_kwota = (inwestycja.kwota * mnozniki[inwestycja.poziom_ryzyka]) #obliczenie wygranej na podstawie kwoty i mnoznika
        zmiana_salda = wygrana_kwota - inwestycja.kwota #wygrana, dodajemy wygrana_kwota do salda, ale odejmujemy kwote, bo uzytkownik ja postawil
        wynik = "Zysk! Prognoza była trafna!"
    else:
        zmiana_salda = -inwestycja.kwota #przegrana, odejmujemy kwotę od salda
        wynik = "Straciłeś! Prognoza nie była trafna."

    zaktualizowany_uzytkownik = crud.zmien_saldo(db, uzytkownik_id=inwestycja.uzytkownik_id, kwota=zmiana_salda)
        
    return {
        "status_inwestycji": wynik,
        "wylosowany_indeks": wylosowana,
        "twoja_prognoza": inwestycja.prognoza,
        "nowe_saldo": zaktualizowany_uzytkownik.saldo
    }


@router.post("/wplata", response_model=schemas.UzytkownikResponse)
def wplac_srodki(wplata: schemas.PaczkaWplaty, db: Session = Depends(get_db)):
    #sprawdzenie czy uzytkownik istnieje
    uzytkownik = crud.pobierz_uzytkownika(db, uzytkownik_id=wplata.uzytkownik_id)
    if not uzytkownik:
        raise HTTPException(status_code=404, detail="Nie znaleziono takiego uzytkownika")
    
    #sprawdzenie czy kwota doladowania jest dodatnia
    if wplata.kwota <= 0:
        raise HTTPException(status_code=400, detail="Kwota doładowania musi być większa niż 0")
    
    #aktualizacja salda uzytkownika w bazie danych

    zaktualizowany_uzytkownik = crud.zmien_saldo(db, uzytkownik_id=wplata.uzytkownik_id, kwota=wplata.kwota)
    return zaktualizowany_uzytkownik
