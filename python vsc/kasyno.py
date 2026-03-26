import random
import json

class Kasyno:
    def __init__(self):
        try:
            with open("zapis_gry.json", "r") as plik:
                wczytany_stan = json.load(plik)
                self.saldo = wczytany_stan["saldo"]
                self.historia_gier = wczytany_stan["historia_gier"]
        except (FileNotFoundError, json.JSONDecodeError):
            print("Nie znaleziono pliku z zapisem gry lub plik jest uszkodzony, ustawiam saldo na domyślną wartość 100zł!")
            self.saldo = 100
            self.historia_gier = []
        self.mnozniki = {"łatwy" : 2, "trudny": 5}


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

        if poziom == 1:
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
            
        elif poziom == 2:
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

        self.zapisz_gre()
            
    def zapisz_gre(self):
        stan_gry = {
            "saldo": self.saldo,
            "historia_gier": self.historia_gier
        }
        with open("zapis_gry.json", "w") as plik:
            json.dump(stan_gry, plik)

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
