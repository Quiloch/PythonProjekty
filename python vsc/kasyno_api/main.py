from fastapi import FastAPI
from routers import router #import router z pliku routers.py

app = FastAPI() #tworzenie instancji aplikacji FastAPI

app.include_router(router) #podlaczenie endpointow z routera do aplikacji