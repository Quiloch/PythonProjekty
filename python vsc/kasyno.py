import random
'''
saldo = 100
mnozniki = {"łatwy" : 2, "trudny": 5}
historia_gier = []

def pobierz_stawke(aktualne_saldo):
    while True:
        try:
            stawka = int(input(f"Podaj stawke, za jaka chcesz zagrac\n"))
            if 0 < stawka <= aktualne_saldo:                    return stawka
            else:
                print("Podana stawka jest nieprawidlowa, sprobuj ponownie")
        except ValueError:
            print("Podana wartosc nie jest liczba")


       
while saldo > 0:
    print("saldo: ", saldo)
    try:
        poziom = int(input(f"Na jakim poziomie chcesz zagrać? (łatwy - 1/trudny - 2)\n"))
        stawka = pobierz_stawke(saldo)
        saldo -= stawka
    except ValueError:
        print("Podana wartosc nie jest liczba")
        continue

    if poziom == 1:
        wylosowana_liczba = random.randint(1,3)
        try:
            typowanie_gracza = int(input("Jaka liczba (1-3) została wylosowana?\n"))
        except ValueError:
            print("Podana wartosc nie jest liczba") 
        if wylosowana_liczba == typowanie_gracza:
            stawka *= mnozniki["łatwy"]
            saldo += stawka
            historia_gier.append("wygrana")
            print("wylosowana liczba to: ", wylosowana_liczba)
        else:
            print("Tym razem sie nie udalo, wylosowana liczba to: ", wylosowana_liczba)
            historia_gier.append("Przegrana")

    elif poziom == 2:
        wylosowana_liczba = random.randint(1,10)
        try:
            typowanie_gracza = int(input(f"Jaka liczba (1-10) została wylosowana\n"))
        except ValueError:
            print("Podana wartosc nie jest liczba")
        if wylosowana_liczba == typowanie_gracza:
            stawka *= mnozniki["trudny"]
            saldo += stawka
            historia_gier.append("wygrana")
            print("wylosowana liczba to: ", wylosowana_liczba)
        else:
            print("Tym razem sie nie udalo, wylosowana liczba to: ", wylosowana_liczba)
            historia_gier.append("Przegrana")
'''
class Kasyno:
    def __init__(self):
        self.saldo = 100
        self.mnozniki = {"łatwy" : 2, "trudny": 5}
        self.historia_gier = []

    def pobierz_stawke(self):
        while True:
            try:
                stawka = int(input(f"Podaj stawke, za jaka chcesz zagrac\n"))
                if 0 < stawka <= self.saldo:
                    return stawka
                else:
                    print("Podana stawka jest nieprawidlowa, sprobuj ponownie")
            except ValueError:
                print("Podana wartosc nie jest liczba")

    def pokaz_historie(self):
        print("Historia gier: ")
        for gra in self.historia_gier:
            print(gra)

    def zagraj(self, poziom, stawka):
        self.saldo -= stawka

        if self.poziom == 1:
            wylosowana_liczba = random.randint(1,3)
            try:
                typowanie_gracza = int(input("Jaka liczba (1-3) została wylosowana?\n"))
                if wylosowana_liczba == typowanie_gracza:
                    stawka *= self.mnozniki["łatwy"]
                    self.saldo += stawka
                    self.historia_gier.append("wygrana")
                    print("wylosowana liczba to: ", wylosowana_liczba)
                else:
                    print("Tym razem sie nie udalo, wylosowana liczba to: ", wylosowana_liczba)
                    self.historia_gier.append("Przegrana")
            except ValueError:
                print("Podana wartosc nie jest liczba")
            
        elif self.poziom == 2:
            wylosowana_liczba = random.randint(1,10)
            try:
                typowanie_gracza = int(input(f"Jaka liczba (1-10) została wylosowana\n"))
                if wylosowana_liczba == typowanie_gracza:
                    stawka *= self.mnozniki["trudny"]
                    self.saldo += stawka
                    self.historia_gier.append("wygrana")
                    print("wylosowana liczba to: ", wylosowana_liczba)
                else:
                    print("Tym razem sie nie udalo, wylosowana liczba to: ", wylosowana_liczba)
                    self.historia_gier.append("Przegrana")
            except ValueError:
                print("Podana wartosc nie jest liczba")
            


moje_kasyno = Kasyno()

print("Witaj w kasynie!")

while moje_kasyno.saldo > 0:
    print(f"\nTwoje saldo: {moje_kasyno.saldo} zł.")
    try:
        poziom = int(input("Na jakim poziomie chcesz zagrać? (łatwy - 1/trudny - 2)\n"))
        if poziom not in [1, 2]:
            print("Nieprawidłowy poziom, wybierz 1 lub 2.")
            continue
    except ValueError:
        print("Podana wartosc nie jest liczba")
        continue
    stawka = moje_kasyno.pobierz_stawke()
    moje_kasyno.zagraj(poziom, stawka)

print("\nBankrut! Koniec gry.")
moje_kasyno.pokaz_historie()
