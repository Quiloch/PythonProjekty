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

def test_rejestracja_nowego_uzytkownika():
    # wyslanie zapytania POST do endpointu rejestracji z danymi nowego uzytkownika tj. w Swaggerze
    odpowiedz = client.post("/rejestracja", json={"nazwa": "TestowyUzytkownik"})

    # sprawdzenie czy odpowiedz ma status 200 (OK)
    assert odpowiedz.status_code == 200

    # rozpakowanie JSON z odpowiedzi
    dane = odpowiedz.json()

    # sprawdzenie czy baza danych zwrocila poprawne dane o nowym uzytkowniku
    assert dane["nazwa"] == "TestowyUzytkownik"
    assert dane["saldo"] == 100
    assert "id" in dane # sprawdzenie czy  baza na pewno nadala ID
    
def test_sprawdz_konto_gracza():
    # sprawdzenie endpointu GET dla gracza o ID=1
    odpowiedz = client.get("/konto/1")

    # sprawdzenie czy odpowiedz ma status 200 (OK)
    assert odpowiedz.status_code == 200

    # rozpakowanie JSON z odpowiedzi i sprawdzenie danych
    dane = odpowiedz.json()
    assert dane["id"] == 1
    assert dane["saldo"] == 100