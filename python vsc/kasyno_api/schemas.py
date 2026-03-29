from pydantic import BaseModel

class PaczkaZakladu(BaseModel):
    poziom: int
    stawka: int
    typowanie: int

class PaczkaDoladowania(BaseModel):
    kwota: int