import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Wczytanie zmiennych środowiskowych z pliku .env
load_dotenv()

# Utworzenie pliku bazy danych kasyno.db w tym samym katalogu
# Wyciagniecie adresu bazy danych z pliku
SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL")

# Stworzenie silnika, ktory bedzie wykonywal komendy SQL
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Stworzenie mechanizmu do tworeznia sesji, ktory bedzie uzywany do komunikacji z baza danych
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Stworzenie klasy BAZOWEJ, po ktorej beda dziedziczyc wszystkie tabele
Base = declarative_base()
