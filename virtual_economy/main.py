from fastapi import FastAPI
from routers import router #import router z pliku routers.py
import models #import modeli z pliku models.py
from database import engine #import silnika bazy danych z pliku database.py

#Stworzenie tabel w bazie danych na podstawie modeli
models.Base.metadata.create_all(bind=engine)

app = FastAPI() #tworzenie instancji aplikacji FastAPI

app.include_router(router) #podlaczenie endpointow z routera do aplikacji