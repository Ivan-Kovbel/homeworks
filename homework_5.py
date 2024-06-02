import os

NUM = "numbers.txt"

def show_menu():
    print("\n" + '*' * 45)
    print("           МЕНЮ СИСТЕМИ ОБЛІКУ ФАЙЛІВ")
    print('*' * 45)

def write_numbers_to_file():
    with open(NUM, "w") as file:
        file.writelines(f"{number}\n" for number in range(101))
    print(f"Числа від 0 до 100 записані у файл '{NUM}'")

def read_text_file():
    filename = input("Введіть назву файлу для читання: ")
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                content = file.read()
                print("Зміст файлу:")
                print(content)
        except Exception as e:
            print(f"Помилка при читанні файлу: {e}")
    else:
        print("Файл не знайдено. Перевірте назву файлу та повторіть спробу.")

def copy_image_file():
    source_image = input("Введіть назву файлу зображення: ")
    if os.path.exists(source_image):
        try:
            with open(source_image, "rb") as file:
                image_data = file.read()
            print("Дані зображення зчитані.")
            return image_data
        except Exception as e:
            print(f"Помилка при зчитуванні файлу: {e}")
    else:
        print("Файл зображення не знайдено. Перевірте назву файлу та повторіть спробу.")
    return None

def write_image_data(image_data):
    if image_data is not None:
        try:
            with open("1.png", "wb") as file:
                file.write(image_data)
            print("Дані успішно записані у файл '1.png'")
        except Exception as e:
            print(f"Помилка при записі даних у файл: {e}")
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
            read_text_file()
        elif choice == '3':
            image_data = copy_image_file()
        elif choice == '4':
            write_image_data(image_data)
        elif choice == 'q':
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір. Будь ласка, спробуйте ще раз.")

main()