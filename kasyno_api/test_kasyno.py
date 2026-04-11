from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from main import app
from database import Base
from routers import get_db

# stworzenie osobnej bazy danych dla testow, aby nie ingerowac w glowna baze danych
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_kasyno.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# utworzenie pustych tabel w bazie danych testowej
Base.metadata.create_all(bind=engine)

# utworzenie funkcji, ktora bedzie zwracac sesje do bazy danych testowej
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

# podmiana bazy danych w aplikacji na baze testowa
app.dependency_overrides[get_db] = override_get_db

# utworzenie wirtualnego klienta, ktory bedzie udawal uzytkownika korzystajacego z API
client = TestClient(app)

def test_pelny():
    # wyslanie zapytania POST do endpointu rejestracji z danymi nowego uzytkownika
    # test 1: rejestracja nowego uzytkownika
    rejestracja = client.post("/rejestracja", json={"nazwa": "TestowyUzytkownik"})
    # sprawdzenie czy odpowiedz ma status 200 (OK)
    assert rejestracja.status_code == 200
    # rozpakowanie JSON z odpowiedzi
    id_gracza = rejestracja.json()["id"]
    
    # test 2: funkcja doladowania
    doladowanie = client.post("/doladuj", json={"gracz_id": id_gracza, "kwota": 100})
    assert doladowanie.status_code == 200
    assert doladowanie.json()["saldo"] == 200

    # test 3: za duza stawka
    stawka_blad = client.post("/zagraj", json={
        "gracz_id": id_gracza,
        "poziom": 1,
        "stawka": 5000,
        "typowanie": 1
    })
    
    assert stawka_blad.status_code == 400
    assert "Nie masz wystarczająco środków na koncie!" in stawka_blad.json()["detail"]

