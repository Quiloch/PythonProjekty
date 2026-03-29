#CRUD - Create, Read, Update, Delete
from sqlalchemy.orm import Session
import models, schemas

#Tworzenie nowego gracza (C)
def stworz_gracza(db: Session, gracz: schemas.GraczCreate):
    #Stworzenie obiektu gracza (saldo zostaje pominiete i automatycznie bedzie ustawione na 100)
    nowy_gracz = models.Gracz(nazwa=gracz.nazwa)

    #Dodanie gracza do bazy danych
    db.add(nowy_gracz)

    #Zatwierdzenie zmian w bazie danych
    db.commit()

    #Odswiezenie obiektu gracza, aby uzyskac jego id
    db.refresh(nowy_gracz)

    return nowy_gracz


#Pobieranie gracza po id (R)
def pobierz_gracza(db: Session, gracz_id: int):
    #Przetlumaczenie na SQL: SELECT * FROM gracz WHERE id = gracz_id)
    return db.query(models.Gracz).filter(models.Gracz.id == gracz_id).first()
