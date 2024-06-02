items = []
def print_separator():
    print("=" * 90)
def display_item(item):
    print("{:<20} {:<10} {:<10} {:<40}".format(item['name'], item['price'], item['balance'], item['description']))
def display_items(items):
    print_separator()
    print("{:<20} {:<10} {:<10} {:<40}".format("Назва", "Вартість", "На складі", "Опис товару"))
    for item in items:
        display_item(item)
    print_separator()
def add_item():
    print("-" * 45)
    print("---------- Додавання нового товару ----------")
    name = input("Введіть назву товару: ").capitalize()
    while True:
        try:
            price = float(input("Введіть вартість одиниці товару: "))
            break
        except ValueError:
            print("Будь ласка, введіть правильну вартість (число з комою).")
    while True:
        try:
            balance = int(input("Введіть кількість товару на складі: "))
            break
        except ValueError:
            print("Будь ласка, введіть правильну кількість (ціле число).")
    description = input("Введіть короткий опис товару: ")
    items.append({"name": name, "price": price, "balance": balance, "description": description})
    print("---------- Товар додано! ----------")
    print("-" * 45)
def choose_item():
    item_number = input("Вкажіть порядковий номер товару: ")
    if item_number.isdigit() and 0 < int(item_number) <= len(items):
        item_number = int(item_number) - 1
        while True:
            print(f"\nОбраний товар: {items[item_number]['name']}")
            print_separator()
            print("{:<20} {:<10} {:<10} {:<40}".format("Назва", "Вартість", "На складі", "Опис товару"))
            display_item(items[item_number])
            print_separator()
            choice = input("""Можливі дії з обраним товаром
[1]-переглянути [2]-редагувати [3]-видалити [q]-головне меню
Оберіть дію: """).lower()
            if choice == '1':
                continue
            elif choice == '2':
                items[item_number].update({"name": input("Введіть нову назву товару: ").capitalize()})
                while True:
                    try:
                        items[item_number]["price"] = float(input("Введіть нову вартість одиниці товару: "))
                        break
                    except ValueError:
                        print("Будь ласка, введіть правильну вартість (число з комою).")
                while True:
                    try:
                        items[item_number]["balance"] = int(input("Введіть нову кількість товару на складі: "))
                        break
                    except ValueError:
                        print("Будь ласка, введіть правильну кількість (ціле число).")
                items[item_number]["description"] = input("Введіть новий короткий опис товару: ")
                print(f"Товар з порядковим номером {item_number + 1} змінено!")
            elif choice == '3':
                print(f"Видалення товару '{items[item_number]['name']}'.")
                if input("Введіть Y для підтвердження: ").lower() == 'y':
                    items.pop(item_number)
                    print("Товар видалено!")
                    break
            elif choice == 'q':
                break
            else:
                print("Неправильний вибір. Будь ласка, спробуйте ще раз.")
def find_item():
    search_term = input("Введіть назву товару для пошуку: ").capitalize()
    found_items = [item for item in items if search_term in item['name']]
    if found_items:
        print("\nЗнайдені товари:")
        display_items(found_items)
    else:
        print("Товар не знайдено.")
while True:
    print("")
    print('*' * 45)
    print("           СИСТЕМА ОБЛІКУ ТОВАРІВ")
    print('-' * 45)
    print(f"Всього товарів додано: {len(items)}")
    print('*' * 45)
    choice = input("""Можливі дії 
[1]-перегляд [2]-додати [3]-обрати [4]-знайти [q]-завершити
Оберіть дію: """)
    if choice == '1':
        display_items(items)
    elif choice == '2':
        add_item()
    elif choice == '3':
        choose_item()
    elif choice == '4':
        find_item()
    elif choice == 'q':
        break
    else:
        print("Неправильний вибір. Будь ласка, спробуйте ще раз.")
