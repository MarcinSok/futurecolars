# program do obsługi ładowarki paczek

print("Program do obsługi ładowarki paczek")

# pobieranie liczby paczek do wysłania
num_of_packages = int(input("Ile paczek chcesz wysłać? "))

# zmienna przechowująca aktualną wagę paczki
package_weight = 0

# zmienna przechowująca wagę wszystkich paczek
total_weight = 0

# lista przechowująca informacje o każdej paczce
packages = []

# pętla dodająca elementy do paczek
for i in range(num_of_packages):
    item_weight = float(input(f"Podaj wagę elementu nr {i+1}: "))
    
    # jeżeli waga elementu jest poza dopuszczalnym zakresem, zakończ dodawanie paczek
    if item_weight < 1 or item_weight > 10:
        print("Niedozwolona waga elementu. Dodawanie paczek zakończone.")
        break
    
    # jeżeli waga elementu przekroczy 20kg, dodaj element do nowej paczki
    if package_weight + item_weight > 20:
        packages.append(package_weight)
        total_weight += package_weight
        package_weight = 0
    
    # dodawanie elementu do paczki
    package_weight += item_weight

# dodanie ostatniej paczki do listy
packages.append(package_weight)
total_weight += package_weight

# wyświetlenie podsumowania
print("\nPodsumowanie:")
print(f"Liczba paczek wysłanych: {len(packages)}")
print(f"Liczba kilogramów wysłanych: {total_weight}")
empty_weight = num_of_packages * 20 - total_weight
print(f"Suma pustych kilogramów: {empty_weight}")

# znalezienie paczki z największą ilością pustych kilogramów
max_empty_weight = 0
max_empty_package = 0
for i, package in enumerate(packages):
    empty_weight = 20 - package
    if empty_weight > max_empty_weight:
        max_empty_weight = empty_weight
        max_empty_package = i + 1

print(f"Paczka z największą ilością pustych kilogramów: {max_empty_package} ({max_empty_weight}kg)")