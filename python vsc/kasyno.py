import random

saldo = 100
mnozniki = {"łatwy" : 2, "trudny": 5}
historia_gier = []

def pobierz_stawke(aktualne_saldo):
    while True:
        try:
            stawka = int(input(f"Podaj stawke, za jaka chcesz zagrac\n"))
            if 0 < stawka <= aktualne_saldo:
                return stawka
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
