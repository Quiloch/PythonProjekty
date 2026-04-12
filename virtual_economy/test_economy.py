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
    id_uzytkownika = rejestracja.json()["id"]
    
    # test 2: funkcja doladowania
    wplata = client.post("/wplata", json={"uzytkownik_id": id_uzytkownika, "kwota": 100})
    assert wplata.status_code == 200
    assert wplata.json()["saldo"] == 200

    # test 3: za duza kwota
    inwestycja_blad = client.post("/inwestuj", json={
        "uzytkownik_id": id_uzytkownika,
        "poziom_ryzyka": 1,
        "kwota": 5000,
        "prognoza": 1
    })
    
    assert  inwestycja_blad.status_code == 400
    assert "Nie masz wystarczająco środków na koncie!" in inwestycja_blad.json()["detail"]

