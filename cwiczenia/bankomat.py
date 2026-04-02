'''
def wyplac_pieniadze(saldo, kwota):
    while True:
        try:
            if(kwota <= saldo):
                nowe_saldo = saldo - kwota
                return nowe_saldo
                break
            else:
                print("Nie masz tyle pieniedzy na koncie, aby je wyplacic.") 
                return saldo
                break
        except ValueError:
            print("Podana wartość nie jest liczbą.")
            

moje_konto = 1000
moje_konto = wyplac_pieniadze(moje_konto, 300)
print(moje_konto)
'''
class KontoBankowe:
    def __init__(self, wlasciciel, saldo):
        self.wlasciciel = wlasciciel
        self.saldo = saldo
        self.historia = []

    def wplac(self, kwota):
        self.kwota = kwota
        self.saldo += self.kwota
        self.historia.append(f"Wpłata: {self.kwota} zł.")
        print(f"Aktualne saldo: {self.saldo} zł.")
    
    def wyplac(self, kwota):
        self.kwota = kwota
        if self.kwota <= self.saldo:
            self.saldo -= self.kwota
            self.historia.append(f"Wypłata: {self.kwota} zł.")
            print(f"Aktualne saldo: {self.saldo} zł.")
        else:
            print("Błąd: brak wystarczających środków na koncie.")
        
    def pokaz_historie(self):
        print("Historia transakcji:")
        for transakcja in self.historia:
            print(transakcja)

konto_testowe = KontoBankowe("Jan Kowalski", 100)
konto_testowe.wplac(50)
konto_testowe.wyplac(30)
konto_testowe.wyplac(500)
konto_testowe.pokaz_historie()