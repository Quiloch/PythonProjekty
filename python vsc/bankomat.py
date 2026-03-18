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
