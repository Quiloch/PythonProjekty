class Samochod:
    def __init__(self, marka, model, max_predkosc):
        self.marka = marka
        self.model = model
        self.predkosc = 0
        self.max_predkosc = max_predkosc

    def przyspiesz(self, wartosc):        
        if self.predkosc + wartosc > self.max_predkosc:
            self.predkosc = self.max_predkosc
            print(f"Osiągnąłeś maksymalną prędkość {self.max_predkosc} km/h!")
        else:
            self.predkosc += wartosc
            print(f"Twoje auto {self.marka} {self.model} przyspiesza! Aktualna predkosc to {self.predkosc} km/h")
    
    def hamuj(self):
        self.predkosc = 0
        print(f"Zatrzymujesz się. Prędkość: {self.predkosc} km/h")

class SamochodElektryczny(Samochod):
    def __init__(self, marka, model, max_predkosc, poziom_baterii):
        super().__init__(marka, model, max_predkosc)
        self.poziom_baterii = poziom_baterii
    
    def naladuj(self):
        self.poziom_baterii = 100
        print(f"Bateria naladowana do 100%")
    
moje_auto = Samochod("Toyota", "Corolla", 180)
moje_auto.przyspiesz(50)
moje_auto.przyspiesz(30)
moje_auto.hamuj()

tesla = SamochodElektryczny("Tesla", "Model S", 250, 40)
tesla.przyspiesz(300)
tesla.naladuj()