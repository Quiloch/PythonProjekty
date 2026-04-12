from sqlalchemy import Column, Integer, String #import potrzebny do tworzenia kolumn
from database import Base #import Base z pliku database.py

class Gracz(Base):
    __tablename__ = "gracze" #nazwa tabeli

    id = Column(Integer, primary_key=True, index=True) #kolumna id, klucz główny
    nazwa = Column(String, index=True) #kolumna z nazwą
    saldo = Column(Integer) #kolumna z saldem
    


