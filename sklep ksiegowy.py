print("\nWitam w systemie księgowym!\n\nDostępne opcje:")
print("\n'saldo' - Zaktualizuj stan salda.")
print("'sprzedaz' - Sprzedaż produktów w magazynie.")
print("'zakup' - Kup nowe produkty do magazynu.")
print("'konto' - Wyświetl stan konta.")
print("'lista' - Wyświetl stan magazynu.")
print("'magazyn' - Wyświetl stan magazynu. dla konkretnego produktu.")
print("'przeglad' - Wyświetl historię magazynu.")
print("'koniec' - Zakończ działanie programu.")

opcja = ""
magazyn, saldo, historia = data

# saldo = 1000.00
# magazyn = {
#     "plecak": {"cena": 20.50, "ilosc": 16},
#     "piłka": {"cena": 15.50, "ilosc": 85},
#     "sanki": {"cena": 40.50, "ilosc": 33},
#     "buty": {"cena": 100.50, "ilosc": 11},
# }
# historia = []

while opcja != "koniec":
    opcja = input("\n--Menu główne-- \n\nPodaj opcję: ")

    if opcja == "saldo":
        print(f"\nObecny stan salda wynosi: {saldo} PLN")
        print("\nDostępne opcje:")
        print("\ndodaj - dodaj kwotę do konta")
        print("odejmij - odejmij kwotę z konta\n")

        opcja_saldo = input("Podaj opcję 'dodaj' lub 'odejmij': ")
        if opcja_saldo == "dodaj":
            kwota = float(input("Podaj kwotę do dodania: "))
            saldo += kwota
            historia.append(f"[{opcja} -> {opcja_saldo}] Dodano {kwota} PLN")
            print(f"Saldo zostało zaktualizowane: {saldo} PLN. Powrót do menu głównego.")
        elif opcja_saldo == "odejmij":
            kwota = float(input("Podaj kwotę do odjęcia: "))
            saldo -= kwota
            historia.append(f"[{opcja} -> {opcja_saldo})] Odjęto {kwota} PLN")
            print(f"Saldo zostało zaktualizowane: {saldo} PLN. Powrót do menu głównego")
        else:
            print("Błędna komenda. Wpisz 'dodaj' lub 'odejmij'.")

    elif opcja == "sprzedaz":
        produkt = input("Podaj nazwę produktu: ")
        cena = float(input("Podaj cenę produktu: "))
        ilosc = int(input("Podaj ilosc produktu: "))

        if produkt in magazyn:
            if magazyn[produkt]["ilosc"] >= ilosc:
                magazyn[produkt]["ilosc"] -= ilosc
                saldo += cena * ilosc
                historia.append(f"[{opcja}] Sprzedano {ilosc} sztuk {produkt} za {cena} PLN")
                print(f"Saldo po operacji: {saldo} PLN")
            else:
                print("Nie ma odpowiedniej ilości na magazynie!")
        else:
            print(f"\nNie ma produktu '{produkt}' w magazynie! Powrót do Menu Głównego.")

    elif opcja == "zakup":
        produkt_buy = input("Podaj nazwę produktu: ")
        if produkt_buy in magazyn:
            print("Nie można dodać tego samego produktu!")
        else:
            cena_buy = float(input("Podaj cenę produktu: "))
            ilosc_buy = int(input("Podaj ilosc produktu: "))
            if cena_buy * ilosc_buy >= saldo:
                print("Brak środków na koncie, operacja anulowana.")
            else:
                magazyn[produkt_buy] = {"cena": cena_buy, "ilosc": ilosc_buy}
                saldo -= cena_buy * ilosc_buy
                historia.append(f"[{opcja}] Kupiono {ilosc_buy} sztuk {produkt_buy} za {cena_buy} PLN")
                print(f"Produkt dodany do magazynu. Saldo po operacji: {saldo}")

    elif opcja == "konto":
        print(f"Stan konta: {saldo:.2f} PLN")
    elif opcja == "lista":
        print("Stan magazynu:\n")
        for produkt, dane in magazyn.items():
            print(f"{produkt} - cena: {dane['cena']}, ilosc : {dane['ilosc']}")
    elif opcja == "magazyn":
        produkt = input("Podaj nazwę produktu: ")
        if produkt in magazyn:
            print(f"{produkt} - cena: {magazyn[produkt]['cena']} PLN, ilosc: {magazyn[produkt]['ilosc']}")
        else:
            print(f"Nie ma produktu '{produkt}' w magazynie!")
    elif opcja == "przeglad":

        print("Podaj zakres przeglądu\n")
        od = input("Podaj początek zakresu (od zera): ")
        do = input("Podaj koniec zakresu: ")
        if od == "" and do == "":
            for akcja in historia:
                print(akcja)
        elif od == "":
            for akcja in historia[:int(do)]:
                print(akcja)
        elif do == "":
            for akcja in historia[int(od):]:
                print(akcja)
        elif int(od) > len(historia) or int(do) > len(historia):
            print(f"Zakres przeglądu jest poza zakresem historii akcji. Liczba wpisów w historii wynosi: {len(historia)}")
        elif int(od) > int(do):
            print(f"Zakres przeglądu jest poza zakresem historii akcji. Liczba wpisów w historii wynosi: {len(historia)}")
        elif int(do) == int(do):
            print(f"Zakres przeglądu jest poza zakresem historii akcji. Liczba wpisów w historii wynosi: {len(historia)}")
        elif int(od) < 0 or int(do) < 0:
            print(f"Zakres przeglądu jest poza zakresem historii akcji. Liczba wpisów w historii wynosi: {len(historia)}")

    elif opcja == "koniec:":
        break
    else:
        print("\nNieprawidłowa opcja.\n\n--Powrót do Menu Głównego--")