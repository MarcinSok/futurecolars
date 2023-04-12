uczniowie = []
nauczyciele = []
wychowawcy = []

while True:
    print("Wybierz jedną z następujących komend: utwórz, zarządzaj, koniec")
    komenda = input()

    if komenda == "utwórz":
        while True:
            print("Wybierz jedną z następujących opcji: uczeń, nauczyciel, wychowawca, koniec")
            opcja = input()

            if opcja == "uczeń":
                imie_nazwisko = input("Podaj imię i nazwisko ucznia: ")
                klasa = input("Podaj nazwę klasy: ")
                uczniowie.append({"imię i nazwisko": imie_nazwisko, "klasa": klasa})

            elif opcja == "nauczyciel":
                imie_nazwisko = input("Podaj imię i nazwisko nauczyciela: ")
                przedmiot = input("Podaj nazwę przedmiotu: ")
                klasy = []
                while True:
                    klasa = input("Podaj nazwę klasy, którą prowadzi nauczyciel (wpisz 'koniec', aby zakończyć): ")
                    if klasa == "koniec":
                        break
                    klasy.append(klasa)
                nauczyciele.append({"imię i nazwisko": imie_nazwisko, "przedmiot": przedmiot, "klasy": klasy})

            elif opcja == "wychowawca":
                imie_nazwisko = input("Podaj imię i nazwisko wychowawcy: ")
                klasa = input("Podaj nazwę klasy, którą prowadzi wychowawca: ")
                wychowawcy.append({"imię i nazwisko": imie_nazwisko, "klasa": klasa})

            elif opcja == "koniec":
                break

            else:
                print("Nieprawidłowa opcja")

    elif komenda == "zarządzaj":
        while True:
            print("Wybierz jedną z następujących opcji: klasa, uczeń, nauczyciel, wychowawca, koniec")
            opcja = input()

            if opcja == "klasa":
                klasa = input("Podaj nazwę klasy: ")
                uczniowie_w_klasie = [u for u in uczniowie if u["klasa"] == klasa]
                wychowawca_klasy = [w for w in wychowawcy if w["klasa"] == klasa][0]["imię i nazwisko"]
                print(f"Uczniowie klasy {klasa}:")
                for u in uczniowie_w_klasie:
                    print(u["imię i nazwisko"])
                print(f"Wychowawca klasy {klasa}: {wychowawca_klasy}")

            elif opcja == "uczeń":
                imie_nazwisko = input("Podaj imię i nazwisko ucznia: ")
                uczen = [u for u in uczniowie if u["imię i nazwisko"] == imie_nazwisko][0]
               
