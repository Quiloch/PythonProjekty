from pydantic import BaseModel, ConfigDict

class PaczkaZakladu(BaseModel):
    gracz_id: int #Dodany parametr, aby moc identyfikowac gracza
    poziom: int
    stawka: int
    typowanie: int

class PaczkaDoladowania(BaseModel):
    gracz_id: int #Dodany parametr, aby moc identyfikowac gracza
    kwota: int

#odebrane dane z formularza rejestracji
class GraczCreate(BaseModel):
    nazwa: str
    
#dane do wyslania do gracza
class GraczResponse(BaseModel):
    id: int
    nazwa: str
    saldo: int

    model_config = ConfigDict(from_attributes=True)

