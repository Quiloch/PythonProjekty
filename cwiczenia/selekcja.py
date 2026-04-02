def filtruj_wiek(kolejka_klubowa):
    wpuszczeni, odrzuceni = [], []
    kolejka_klubowa.sort()
    for wiek in kolejka_klubowa:
        if wiek >= 18:
            wpuszczeni.append(wiek)
        else:
            odrzuceni.append(wiek)
    return wpuszczeni, odrzuceni

dzisiejsi_goscie = [16, 21, 19, 15]
ok, nie_ok = filtruj_wiek(dzisiejsi_goscie)
print(f"wpuszczeni: {ok}\n odrzuceni: {nie_ok}")