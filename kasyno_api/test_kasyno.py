from fastapi.testclient import TestClient
from main import app

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
    #assert dane["saldo"] == 100