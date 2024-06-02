def remove_duplicates(lst):
    return list(set(lst))
def find_unique_elements(lst):
    return set(lst)
def find_intersection(lst1, lst2):
    return tuple(set(lst1) & set(lst2))
def print_separator():
    print("=" * 40)
def action1():
    print("Ви обрали дію 1: Позбутись дублювання у списках")
    try:
        data = list(map(int, input("Введіть числа для першого списку через кому: ").split(',')))
        data2 = list(map(int, input("Введіть числа для другого списку через кому: ").split(',')))
        unique_data = remove_duplicates(data)
        unique_data2 = remove_duplicates(data2)
        print(f"Список 'data' без дублювання: {unique_data}")
        print(f"Список 'data2' без дублювання: {unique_data2}")
    except ValueError:
        print("Введено некоректні дані. Спробуйте ще раз.")
def action2():
    print("Ви обрали дію 2: Знайти унікальні елементи для списків")
    try:
        data = list(map(int, input("Введіть числа для першого списку через кому: ").split(',')))
        data2 = list(map(int, input("Введіть числа для другого списку через кому: ").split(',')))
        unique_elements_data = find_unique_elements(data)
        unique_elements_data2 = find_unique_elements(data2)
        print(f"Унікальні елементи у 'data': {unique_elements_data}")
        print(f"Унікальні елементи у 'data2': {unique_elements_data2}")
    except ValueError:
        print("Введено некоректні дані. Спробуйте ще раз.")
def action3():
    print("Ви обрали дію 3: Знайти перетин між списками та сформувати із нього кортеж")
    try:
        data = list(map(int, input("Введіть числа для першого списку через кому: ").split(',')))
        data2 = list(map(int, input("Введіть числа для другого списку через кому: ").split(',')))
        intersection_tuple = find_intersection(data, data2)
        print(f"Перетин між 'data' і 'data2' у вигляді кортежу: {intersection_tuple}")
    except ValueError:
        print("Введено некоректні дані. Спробуйте ще раз.")
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
        if choice == '1':
            action1()
        elif choice == '2':
            action2()
        elif choice == '3':
            action3()
        elif choice == 'q':
            print("Завершення програми...")
            break
        else:
            print("Неправильний вибір, спробуйте ще раз.")
main_menu()

