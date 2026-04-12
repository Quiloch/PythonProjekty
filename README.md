# Virtual Economy API

Proste API backendowe do obsługi wirtualnej ekonomii, zarządzania portfelami użytkowników oraz symulacji inwestycji. Projekt powstał w celu praktycznego zastosowania dobrych praktyk inżynierii oprogramowania.

Aplikacja symuluje architekturę nowoczesnych systemów finansowych: posiada wyraźny podział na warstwy (routing, operacje CRUD, modele bazy danych), korzysta z relacyjnej bazy danych, weryfikuje dane przychodzące i jest pokryta testami automatycznymi.

## Wykorzystane technologie

* **Python 3.11+**
* **FastAPI** (tworzenie endpointów i automatyczna dokumentacja Swagger)
* **SQLAlchemy** (obsługa bazy danych poprzez mapowanie obiektowo-relacyjne ORM)
* **SQLite** (lekka, plikowa baza danych)
* **Pydantic** (walidacja paczek JSON i kontrola typów)
* **pytest** (zautomatyzowane testy jednostkowe z izolowaną bazą testową)
* **GitHub Actions** (Continuous Integration - automatyczne testowanie kodu w chmurze)
* **python-dotenv** (zarządzanie zmiennymi środowiskowymi)

## Główne funkcjonalności

1. **Rejestracja użytkownika** (przypisanie unikalnego ID oraz początkowego salda 100 jednostek).
2. **Sprawdzanie stanu konta** (odczyt danych z bazy).
3. **Wpłaty** (transakcje modyfikujące saldo).
4. **Symulacja Inwestycji** (procesowanie transakcji na różnych poziomach ryzyka z symulacją zmienności rynku). Logika operacji jest zabezpieczona przed ujemnymi stawkami oraz działaniami bez posiadania wystarczających środków na koncie.
5. **Bezpieczeństwo konfiguracji** (wrażliwe dane i adresy odczytywane są z ukrytego pliku `.env`).

## Jak uruchomić projekt lokalnie?

1. Sklonuj repozytorium na swój komputer.
2. Upewnij się, że masz zainstalowanego Pythona, a następnie zainstaluj wymagane biblioteki:
   ```bash
   pip install -r requirements.txt
3. Stwórz plik .env w głównym folderze projektu i dodaj w nim adres bazy danych:
   ```
   DATABASE_URL=sqlite:///./economy.db
5. Uruchom serwer developerski Uvicorn:
    ```
    uvicorn main:app --reload

## Testowanie API
Projekt posiada zautomatyzowane testy, które dzięki mechanizmowi dependency overrides działają na odizolowanej bazie danych (test_economy.db).

Aby uruchomić testy, wpisz w terminalu:
    
    pytest

Aby przetestować aplikację manualnie z poziomu interfejsu graficznego, po uruchomieniu serwera należy wejść w przeglądarce pod adres:
    
    http://localhost:8000/docs
