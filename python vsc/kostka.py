import random

def rzut_koscia(ilosc_scian):
    wynik = random.randint(1, ilosc_scian)
    print(wynik)

lista_rzutow = []
for i in range(0,3):
    lista_rzutow.append(rzut_koscia(6))
    i += 1


#rzut_koscia(6)
#rzut_koscia(20)
#rzut_koscia(100)