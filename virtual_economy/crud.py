#CRUD - Create, Read, Update, Delete
from sqlalchemy.orm import Session
import models, schemas

#Tworzenie nowego gracza (C)
def stworz_uzytkownika(db: Session, uzytkownik: schemas.UzytkownikCreate):
    #Stworzenie obiektu gracza
    nowy_uzytkownik = models.Uzytkownik(nazwa=uzytkownik.nazwa, saldo=100)

    #Dodanie gracza do bazy danych
    db.add(nowy_uzytkownik)

    #Zatwierdzenie zmian w bazie danych
    db.commit()

    #Odswiezenie obiektu gracza, aby uzyskac jego id
    db.refresh(nowy_uzytkownik)

    return nowy_uzytkownik


#Pobieranie uzytkownika po id (R)
def pobierz_uzytkownika(db: Session, uzytkownik_id: int):
    #Przetlumaczenie na SQL: SELECT * FROM uzytkownik WHERE id = uzytkownik_id)
    return db.query(models.Uzytkownik).filter(models.Uzytkownik.id == uzytkownik_id).first()

#Aktualizacja salda (U)
def dodaj_do_salda(db: Session, uzytkownik_id: int, kwota: int):
    uzytkownik = pobierz_uzytkownika(db, uzytkownik_id)

    if uzytkownik:
        uzytkownik.saldo += kwota
        db.commit()
        db.refresh(uzytkownik)
    
    return uzytkownik