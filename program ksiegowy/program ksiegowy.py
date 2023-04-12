# inicjalizacja konta i magazynu
konto = 0
magazyn = {}

# funkcja do pobierania danych od użytkownika
def pobierz_dane():
    dane = input().split()
    return dane[0], float(dane[1]), int(dane[2])

# funkcja do wyświetlania stanu konta
def pokaz_konto():
    print(f"Stan konta: {konto:.2f}")

# funkcja do wyświetlania stanu magazynu
def pokaz_magazyn():
    nazwa = input("Podaj nazwę produktu: ")
    if nazwa in magazyn:
        cena, ilosc = magazyn[nazwa]
        print(f"{nazwa}: cena={cena:.2f} zł, ilość={ilosc}")
    else:
        print("Nie ma takiego produktu w magazynie")

# funkcja do wyświetlania listy produktów w magazynie
def pokaz_liste():
    print("Stan magazynu:")
    for nazwa, (cena, ilosc) in magazyn.items():
        print(f"{nazwa}: cena={cena:.2f} zł, ilość={ilosc}")

# funkcja do wyświetlania przeglądu operacji
def pokaz_przeglad():
    od = input("Od której operacji? (1 - pierwsza)")
    do = input(f"Do której operacji? (max: {len(historia)})")
    try:
        od = max(1, int(od))
        do = min(len(historia), int(do)) if do else len(historia)
        for i in range(od-1, do):
            print(historia[i])
    except ValueError:
        print("Nieprawidłowe wartości")

# pętla główna programu
while True:
    print("\nDostępne komendy:")
    print("saldo\nsprzedaż\nzakup\nkonto\nlista\nmagazyn\nprzegląd\nkoniec")

    # odczytanie wybranej komendy
    komenda = input("Podaj komendę: ").lower()

    # obsługa komendy "saldo"
    if komenda == "saldo":
        kwota = float(input("Podaj kwotę: "))
        konto += kwota
        historia.append(f"SALDO {kwota:.2f}")

    # obsługa komendy "sprzedaż"
    elif komenda == "sprzedaż":
        nazwa, cena, ilosc = pobierz_dane()
        if nazwa in magazyn and magazyn[nazwa][1] >= ilosc:
            magazyn[nazwa][1] -= ilosc
            konto += cena * ilosc
            historia.append(f"SPRZEDAŻ {nazwa} {cena:.2f} {ilosc}")
        else:
            print("Nie ma wystarczającej ilości produktu w magazynie")

    # obsługa komendy "zakup"
    elif komenda == "zakup":
        nazwa, cena, ilosc = pobierz_dane()
        if konto < cena * ilosc:
            print
