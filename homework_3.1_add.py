def remove_duplicates(lst):
    return list(set(lst))

def find_unique_elements(lst):
    return set(lst)

def find_intersection(lst1, lst2):
    return tuple(set(lst1) & set(lst2))

def print_separator():
    print("=" * 40)

def get_input():
    try:
        data = list(map(int, input("Введіть числа для списку через кому: ").split(',')))
        return data
    except ValueError:
        print("Введено некоректні дані. Спробуйте ще раз.")
        return None

def process_data(action):
    print(f"Ви обрали дію {action}: {actions[action]['message']}")
    data = get_input()
    if data is None:
        return
    data2 = get_input()
    if data2 is None:
        return
    
    result1 = actions[action]['function'](data)
    result2 = actions[action]['function'](data2)
    
    print(f"Результат для 'data': {result1}")
    print(f"Результат для 'data2': {result2}")

def action1(data):
    return remove_duplicates(data)

def action2(data):
    return find_unique_elements(data)

def action3(data):
    return find_intersection(data, data)

actions = {
    '1': {'function': action1, 'message': 'Позбутись дублювання у списках'},
    '2': {'function': action2, 'message': 'Знайти унікальні елементи для списків'},
    '3': {'function': action3, 'message': 'Знайти перетин між списками та сформувати із нього кортеж'},
}

def main_menu():
    while True:
        print_separator()
        print("Головне меню:")
        for key in actions:
            print(f"[{key}] {actions[key]['message']}")
        print("[q] Завершити програму")
        print_separator()
        
        choice = input("Оберіть дію: ").lower()
        if choice in actions:
            process_data(choice)
        elif choice == 'q':
            print("Завершення програми...")
            break
        else:
            print("Неправильний вибір, спробуйте ще раз.")

main_menu()
