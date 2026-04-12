from pydantic import BaseModel, ConfigDict

class PaczkaInwestycji(BaseModel):
    uzytkownik_id: int #Dodany parametr, aby moc identyfikowac uzytkownika
    poziom_ryzyka: int
    kwota: int
    typowanie: int

class PaczkaWplaty(BaseModel):
    uzytkownik_id: int #Dodany parametr, aby moc identyfikowac uzytkownika
    kwota: int

#odebrane dane z formularza rejestracji
class UzytkownikCreate(BaseModel):
    nazwa: str
    
#dane do wyslania do uzytkownika
class UzytkownikResponse(BaseModel):
    id: int
    nazwa: str
    saldo: int

    model_config = ConfigDict(from_attributes=True)

