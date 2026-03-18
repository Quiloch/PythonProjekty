'''
#input i casting

zlotowki = input("Ile masz zlotych?\n")
euro = float(zlotowki) * 4.3
print(f"Za tyle {zlotowki} kupisz {euro} euro!")

#ochroniarz
wiek = input("Ile masz lat?\n")
if(int(wiek) >= 18):
    print("Mozesz obejrzec horror")
elif(int(wiek) > 13 and int(wiek) < 18):
    print("Mozesz obejrzec film akcji, ale nie horror")
else:
    print("Mozesz obejrzec film animowany")

#lista
zakupy = ["sól", "pieprz", "cukier", "mąka"]
print(zakupy[1])

zakupy.append("mleko")
zakupy[0] = "woda"
print(zakupy)

#petle
for produkt in zakupy:
    print(f"Musze kupić {produkt}")

liczba = 10
while liczba%2 == 0 and liczba >= 0:
    print(f"{liczba} jest parzysta")
    liczba -= 2


#bankomat
saldo = 1000
kwota = int(input (f"Twoje saldo wynosi {saldo} zł. Ile chcesz wypłacić?\n"))
if(kwota <= saldo):
    saldo -= kwota
    print(f"Wypłaciłeś {kwota} zł. Twoje saldo wynosi teraz {saldo} zł.")
else:
    print("Nie masz tyle pieniędzy na koncie, aby je wypłacić.")

#selekcja

kolejka = [16, 21, 19, 15, 25, 30, 17, 18]
wpuszczeni, odrzuceni = [], []
for wiek in kolejka:
    if wiek >= 18:
        wpuszczeni.append(wiek)
    else:
        odrzuceni.append(wiek)
print(f"Wpuszczeni: {wpuszczeni}")
print(f"Odrzuceni: {odrzuceni}")


#system logowania
poprawne_haslo = "python123"
proby = 3
while proby > 0:
    haslo = input("Prosze podac haslo:\n")
    if haslo == poprawne_haslo:
        print("Zalogowano")
        break
    else:
        proby -= 1
        print(f"Podano złe hasło. Pozostało {proby} prób.")
        if proby == 0:
            print("Konto zablokowane.")
            break
'''