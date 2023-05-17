users = {
    "uczniowie": [
        {
            "imie": "Marcin",
            "nazwisko": "Grabowski",
            "klasa": "1A"
        },
        {
            "imie": "Ula",
            "nazwisko": "Kwiatkowska",
            "klasa": "1B"
        },
        {
            "imie": "Marek",
            "nazwisko": "goc",
            "klasa": "1C"
        }
    ],
    "nauczyciele": [
        {
            "imie": "Jacek",
            "nazwisko": "kubowicz",
            "przedmiot": "WF",
            "klasa": ["1A", "2C"]
        },
        {
            "imie": "Jerzy",
            "nazwisko": "Stanowski",
            "przedmiot": "fizyka",
            "klasa": ["1A"]
        },
        {
            "imie": "Michał",
            "nazwisko": "Michałowski",
            "przedmiot": "j.polski",
            "klasa": ["1A", "2C"]
        },
    ],
    "wychowawcy:": [
        {
            "imie": "Wiktor",
            "nazwisko": "Lesiak",
            "przedmiot": "chemia",
            "klasa": "1A"
        },
        {
            "imie": "Andrzej",
            "nazwisko": "Binkowski",
            "przedmiot": "historia",
            "klasa": "1B"
        },
    ],
}


def find_student(name, surname):
    for person in users["uczniowie"]:
        if person["imie"] == name and person["nazwisko"] == surname:
            return True
    return False

def find_teacher(name, surname):
    for person in users["nauczyciele"]:
        if person["imie"] == name and person["nazwisko"] == surname:
            return True
    return False

def user_create(user_type):
    if user_type == "uczeń":
        print("\nDodaj ucznia do systemu\n")
        imie = input("Podaj imię: ")
        nazwisko = input("Podaj nazwisko: ")
        klasa = input("Podaj klasę: ")
        users["uczniowie"].append({
            "imie": imie,
            "nazwisko": nazwisko,
            "klasa": klasa
        })
    elif user_type == "nauczyciel":
        klasa_list = []
        print("\nDodaj nauczyciela do systemu\n")
        imie = input("Podaj imię: ")
        nazwisko = input("Podaj nazwisko: ")
        przedmiot = input("Podaj przedmiot: ")
        klasa = input("Podaj klasę: ")
        while klasa != "":
            klasa_list.append(klasa)
            klasa = input("Podaj klasę: ")
        users["nauczyciele"].append({
            "imie": imie,
            "nazwisko": nazwisko,
            "przedmiot": przedmiot,
            "klasa": klasa_list
        })
    elif user_type == "wychowawca":
        print("\nDodanie wychowawcy do systemu\n")
        imie = input("Podaj imię: ")
        nazwisko = input("Podaj nazwisko: ")
        przedmiot = input("Podaj przedmiot: ")
        klasa = input("Podaj klasę: ")
        users["wychowawcy:"].append({
            "imie": imie,
            "nazwisko": nazwisko,
            "przedmiot": przedmiot,
            "klasa": klasa
        })
    else:
        print("Nieznana komenda. Dostępne komendy: 'uczeń', 'nauczyciel', 'wychowawca'")

def user_manage(opcja):

    if opcja == "klasa":
        print("\nInformacja o klasie\n")
        klasa = input("Podaj klasę: ")
        print(f"\nUczniowie w klasie {klasa}\n")
        for uczen in users["uczniowie"]:
            if uczen["klasa"] == klasa:
                print(f"{uczen['imie']} {uczen['nazwisko']}")
        print(f"\nWychowawcy klasy {klasa}: \n")
        for wychowawca in users["wychowawcy:"]:
            if wychowawca["klasa"] == klasa:
                print(f"{wychowawca['imie']} {wychowawca['nazwisko']}")

    elif opcja == "uczeń":
        print("\nInformacja o uczniu\n")
        print("\nLista uczniów w systemie:\n")
        for students in users["uczniowie"]:
            print(students)
        name = input("\nPodaj imię ucznia: ")
        surname = input("Podaj nazwisko ucznia: ")
        result = find_student(name, surname)
        if result is True:
            print(f"\nUczeń {name} {surname} jest w bazie danych."
                  f"\nPrzedmioty na które uczęszcza uczeń i nauczyciel prowadzący:")
            for uczen in users["uczniowie"]:
                if uczen["imie"] == name and uczen["nazwisko"] == surname:
                    klasa = uczen["klasa"]
                    for nauczyciel in users["nauczyciele"]:
                        if klasa in nauczyciel["klasa"]:
                            przedmiot = nauczyciel["przedmiot"]
                            print(f"{przedmiot} - {nauczyciel['imie']} {nauczyciel['nazwisko']}")
        else:
            print("\bBrak ucznia w bazie danych!\b")

    elif opcja == "nauczyciel":
        print("\nInformacja o nauczycielu\nLista nauczycieli:\n ")
        for teachers in users["nauczyciele"]:
            print(teachers)
        teacher_name = input("\nPodaj imię nauczyciela: ")
        teacher_surname = input("\nPodaj nazwisko nauczyciela:  ")
        result = find_teacher(teacher_name, teacher_surname)
        if result is True:
            print(f"\bNauczyciel {teacher_name} {teacher_surname} jest w bazie danych.\b")
            for teacher in users["nauczyciele"]:
                if teacher ["imie"] == teacher_name and teacher["nazwisko"] == teacher_surname:
                    print(f"Nauczyciel {teacher_name} {teacher_surname} prowadzi klasy:")
                    for klasa in teacher["klasa"]:
                        print(klasa)
        else:
            print("\bBrak nauczyciela w bazie danych!\b")

    elif opcja == "wychowawca":
        print("\nInformacja o wychowawcy\nLista wychowawców w systemie:\n ")
        for wychowawca in users["wychowawcy:"]:
            print(wychowawca)
        wychowawca_name = input("\nPodaj imię wychowawcy: ")
        wychowawca_surname = input("Podaj nazwisko wychowawcy: ")
        wychowawca_students = []
        for wychowawca in users["wychowawcy:"]:
            if wychowawca["imie"] == wychowawca_name and wychowawca["nazwisko"] == wychowawca_surname:
                for uczen in users["uczniowie"]:
                    if uczen["klasa"] == wychowawca["klasa"]:
                        wychowawca_students.append(uczen)
        if len(wychowawca_students) == 0:
            print("Dany nauczyciel nie posiada swojej klasy.")
        else:
            print(f"\bUczniowie należący do klasy wychowawcy {wychowawca_name} {wychowawca_surname}:")
            for uczen in wychowawca_students:
                print("{} {}".format(uczen["imie"], uczen["nazwisko"]))
    else:
        print("\nBłędna komenda")

opcja = ""

while opcja != "koniec":
    print("\nSystem zarządzania klasami.\n")
    print("Dostępne opcje: \n\n'utwórz' - Dodaj ucznia/nauczyciela/wychowawcę,"
          " \n'zarządzaj' - Zarządzaj użytkownikami,"
          " \n'koniec' - Zakoncz działanie programu.\n")
    opcja = input("Wybierz opcję: ")
    if opcja == "utwórz":
        print("\nDostępne opcje:\n")
        print("'uczeń' - Dodaj ucznia do systemu,")
        print("'nauczyciel' - Dodaj nauczyciela do systemy,")
        print("'wychowawca' - Dodaj wychowawcę do systemu,")
        print("'koniec' - powrót do menu głównego.")
        user_utworz = ""
        while user_utworz != "koniec":
            user_utworz = input("\nPodaj typ użytkownika: ")
            if user_utworz == "koniec":
                break
            user_create(user_utworz)

    elif opcja == "zarządzaj":
        print("\nWybierz opcję:\n\n'klasa' - Wyświetl uczniów w danej klasie i wychowawcę,"
              "\n'uczeń' - Wyświetl ucznia, jego lekcję i nauczycieli, ktorzy lekcję prowadzą,"
              "\n'nauczyciel' - Wyświetl nauczyciela i przedmioty, które prowadzi,"
              "\n'wychowawca' - Wyświetl wychowawcę i klasę, którą zarządza,"
              "\n'koniec' - Wróć do menu główneo.")
        opcja_zarzadzaj = ""
        while opcja_zarzadzaj != "koniec":
            opcja_zarzadzaj = input("\nWybierz opcję: ")
            if opcja_zarzadzaj == "koniec":
                break
            user_manage(opcja_zarzadzaj)

    elif opcja == "koniec":
        break
    elif opcja == "debug":
        print("Baza użytkowników")
        for users_type in users:
            print(f"{users_type}")
            for user in users[users_type]:
                print(f'{user}')
            print()
    else:
        print("Błąd, nieznana komenda.")

