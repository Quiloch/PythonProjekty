# Kasyno REST API

Proste, ale w pełni funkcjonalne API backendowe do obsługi wirtualnego kasyna. Projekt powstał w celu praktycznego zastosowania dobrych praktyk inżynierii oprogramowania. 

Aplikacja symuluje architekturę prawdziwych systemów finansowych: posiada wyraźny podział na warstwy (routing, operacje CRUD, modele bazy danych), korzysta z relacyjnej bazy danych i rygorystycznie weryfikuje dane przychodzące od użytkownika.

## Wykorzystane technologie

* **Python 3**
* **FastAPI** (błyskawiczne tworzenie endpointów i automatyczna dokumentacja Swagger)
* **SQLAlchemy** (obsługa bazy danych poprzez mapowanie obiektowo-relacyjne ORM)
* **SQLite** (lekka, plikowa baza danych)
* **Pydantic** (walidacja paczek JSON i kontrola typów)
* **Uvicorn** (serwer ASGI)

## Główne funkcjonalności

1. **Rejestracja gracza** (przypisanie unikalnego ID oraz początkowego salda 100 zł).
2. **Sprawdzanie stanu konta** (odczyt danych z bazy).
3. **Doładowanie portfela** (transakcje modyfikujące saldo).
4. **Gra w kasynie** (obstawianie na różnych poziomach trudności). Logika gry jest w pełni zabezpieczona przed ujemnymi stawkami oraz grą bez wystarczających środków na koncie. Operacje finansowe opierają się na bezpiecznych transakcjach bazodanowych.

## Jak uruchomić projekt lokalnie?

1. Sklonuj repozytorium na swój komputer.
2. Upewnij się, że masz zainstalowanego Pythona, a następnie zainstaluj wymagane biblioteki:
   ```bash
   pip install -r requirements.txt
3. Uruchom serwer developerski Uvicorn:
    Bash
    uvicorn main:app --reload
4. Baza danych (kasyno.db) wygeneruje się automatycznie przy pierwszym uruchomieniu.

## Testowanie API
Projekt nie posiada własnego frontendu, ponieważ skupia się wyłącznie na architekturze backendowej. Aby przetestować aplikację, po uruchomieniu serwera wejdź w przeglądarce pod adres:

http://localhost:8000/docs

Otworzy się interaktywna dokumentacja Swagger UI, z poziomu której możesz zakładać konta, wpłacać środki i wysyłać zakłady.