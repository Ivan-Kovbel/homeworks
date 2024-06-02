import os

NUM = "numbers.txt"

def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Сталася помилка: {e}")
    return wrapper

def file_exists_checker(func):
    def wrapper(filename, *args, **kwargs):
        if not os.path.exists(filename):
            print(f"Файл {filename} не знайдено.")
            return
        return func(filename, *args, **kwargs)
    return wrapper

def show_menu():
    print("\n" + '*' * 45)
    print("           МЕНЮ СИСТЕМИ ОБЛІКУ ФАЙЛІВ")
    print('*' * 45)

@exception_handler
def write_numbers_to_file():
    with open(NUM, "w") as file:
        file.writelines(f"{number}\n" for number in range(101))
    print(f"Числа від 0 до 100 записані у файл '{NUM}'")

@exception_handler
@file_exists_checker
def read_text_file(filename):
    with open(filename, "r") as file:
        content = file.read()
        print("Зміст файлу:")
        print(content)

@exception_handler
@file_exists_checker
def copy_image_file(source_image):
    with open(source_image, "rb") as file:
        image_data = file.read()
    print("Дані зображення зчитані.")
    return image_data

@exception_handler
def write_image_data(image_data):
    if image_data is not None:
        with open("1.png", "wb") as file:
            file.write(image_data)
        print("Дані успішно записані у файл '1.png'")
    else:
        print("Дані зображення ще не зчитані. Спочатку скопіюйте дані зображення.")

def main():
    image_data = None
    while True:
        show_menu()
        choice = input("""Можливі дії:
[1]-Записати числа у файл
[2]-Прочитати текстовий файл
[3]-Зчитати дані зображення
[4]-Записати дані зображення у файл '1.png'
[q]-Вийти
Оберіть дію: """)
        print("")

        if choice == '1':
            write_numbers_to_file()
        elif choice == '2':
            filename = input("Введіть назву файлу для читання: ")
            read_text_file(filename)
        elif choice == '3':
            source_image = input("Введіть назву файлу зображення: ")
            image_data = copy_image_file(source_image)
        elif choice == '4':
            write_image_data(image_data)
        elif choice == 'q':
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір. Будь ласка, спробуйте ще раз.")

main()
