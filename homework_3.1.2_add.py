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

def data_processor(func):
    def wrapper():
        print(f"Ви обрали дію: {func.__name__}")
        data = get_input()
        if data is None:
            return
        data2 = get_input()
        if data2 is None:
            return
        
        result1 = func(data)
        result2 = func(data2)
        
        print(f"Результат для 'data': {result1}")
        print(f"Результат для 'data2': {result2}")
    return wrapper

@data_processor
def action1(data):
    return remove_duplicates(data)

@data_processor
def action2(data):
    return find_unique_elements(data)

@data_processor
def action3(data):
    return find_intersection(data, data)

actions = {
    '1': action1,
    '2': action2,
    '3': action3,}

def main_menu():
    while True:
        print_separator()
        print("Головне меню:")
        print("[1] Позбутись дублювання у списках")
        print("[2] Знайти унікальні елементи для списків")
        print("[3] Знайти перетин між списками та сформувати із нього кортеж")
        print("[q] Завершити програму")
        print_separator()
        
        choice = input("Оберіть дію: ").lower()
        if choice in actions:
            actions[choice]()
        elif choice == 'q':
            print("Завершення програми...")
            break
        else:
            print("Неправильний вибір, спробуйте ще раз.")

main_menu()
