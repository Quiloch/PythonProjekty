from pydantic import BaseModel

class PaczkaZakladu(BaseModel):
    poziom: int
    stawka: int
    typowanie: int

class PaczkaDoladowania(BaseModel):
    kwota: int

#odebrane dane z formularza rejestracji
class GraczCreate(BaseModel):
    nazwa: str
    
#dane do wyslania do gracza
class GraczResponse(BaseModel):
    id: int
    nazwa: str
    saldo: int

    #aby pydantic mogl tworzyc obiekty z danych otrzymanych z bazy danych, ktore sa w formie dict
    class Config:
        from_attributes = True