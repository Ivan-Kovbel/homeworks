def print_separator():
    print("=" * 90)

def display_item(item):
    print("{:<20} {:<10} {:<10} {:<40}".format(
        item['name'], item['price'], item['balance'], item['description']))

def display_items(items):
    print_separator()
    print("{:<20} {:<10} {:<10} {:<40}".format(
        "Назва", "Вартість", "На складі", "Опис товару"))
    for item in items:
        display_item(item)
    print_separator()

def get_input(prompt, input_type=str, validation=None, 
              error_message="Неправильний ввод. Спробуйте ще раз."):
    while True:
        try:
            value = input_type(input(prompt))
            if validation and not validation(value):
                raise ValueError
            return value
        except ValueError:
            print(error_message)

class Inventory:
    def __init__(self):
        self.items = []

    def display_items(self):
        display_items(self.items)

    def add_item(self):
        print("-" * 45)
        print("---------- Додавання нового товару ----------")
        name = get_input("Введіть назву товару: ").capitalize()
        price = get_input("Введіть вартість одиниці товару: ", float, 
                          error_message="Будь ласка, введіть правильну вартість (число з комою).")
        balance = get_input("Введіть кількість товару на складі: ", int, 
                            error_message="Будь ласка, введіть правильну кількість (ціле число).")
        description = get_input("Введіть короткий опис товару: ")
        self.items.append({"name": name, "price": price, "balance": balance, "description": description})
        print("---------- Товар додано! ----------")
        print("-" * 45)

    def choose_item(self):
        item_number = int(get_input("Вкажіть порядковий номер товару: ", 
                            int, 
                            lambda x: 0 < x <= len(self.items), 
                            "Неправильний порядковий номер товару. Спробуйте ще раз.")) - 1
        return self.items[item_number]

    def update_item(self, item):
        new_name = get_input("Введіть нову назву товару: ").capitalize()
        new_price = get_input("Введіть нову вартість одиниці товару: ", float,
                          error_message="Будь ласка, введіть правильну вартість (число з комою).")
        new_balance = get_input("Введіть нову кількість товару на складі: ", int,
                            error_message="Будь ласка, введіть правильну кількість (ціле число).")
        new_description = get_input("Введіть новий короткий опис товару: ")

        item['name'] = new_name
        item['price'] = new_price
        item['balance'] = new_balance
        item['description'] = new_description
        print(f"Товар '{item['name']}' змінено!")

    def delete_item(self, item):
        if input(f"Видалення товару '{item['name']}'. Введіть Y для підтвердження: ").lower() == 'y':
            self.items.remove(item)
            print("Товар видалено!")

    def find_item(self):
        search_term = get_input("Введіть назву товару для пошуку: ").capitalize()
        found_items = [item for item in self.items if search_term in item['name']]
        if found_items:
            print("\nЗнайдені товари:")
            display_items(found_items)
            return found_items
        else:
            print("Товар не знайдено.")
            return None

def edit_item(inventory, item):
    inventory.update_item(item)

def remove_item(inventory, item):
    inventory.delete_item(item)

def manage_item(inventory, item):
    while True:
        print("\nВибраний товар:")
        display_item(item)
        choice = input("""\nМожливі дії з обраним товаром:
[1]-редагувати [2]-видалити [q]-повернутися
Оберіть дію: """)
        if choice == '1':
            edit_item(inventory, item)
        elif choice == '2':
            remove_item(inventory, item)
            break
        elif choice == 'q':
            break
        else:
            print("Неправильний вибір. Будь ласка, спробуйте ще раз.")

def print_menu(inventory):
    divider = '*' * 45
    print("")
    print(divider)
    print("           СИСТЕМА ОБЛІКУ ТОВАРІВ")
    print('-' * 45)
    print(f"Всього товарів додано: {len(inventory.items)}")
    print(divider)

def main():
    inventory = Inventory()

    actions = {
        '1': inventory.display_items,
        '2': inventory.add_item,
        '3': lambda: manage_item(inventory, inventory.choose_item()),
        '4': inventory.find_item
    }

    while True:
        print_menu(inventory)
        choice = input("""Можливі дії 
[1]-перегляд [2]-додати [3]-обрати [4]-знайти [q]-завершити
Оберіть дію: """)
        if choice == 'q':
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Неправильний вибір. Будь ласка, спробуйте ще раз.")

main()
