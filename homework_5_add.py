import pickle

def get_data_info(filename):
    with open(filename, "rb") as file:
        return {"filename": filename, "size": len(file.read())}

def add_files(file_info):
    filename = input("Введіть ім'я файлу: ")
    file_info.append(get_data_info(filename))

def save_data(file_info):
    result_file_name = input("Введіть ім'я результативного файлу: ")
    with open(result_file_name, "wb") as result_file:
        for data in file_info:
            with open(data["filename"], "rb") as file:
                result_file.write(file.read())

    with open("info.txt", "wb") as file:
        pickle.dump(file_info, file)

def view_data(file_info):
    for element in file_info:
        print(element)

def decode_data():
    data_file = input("Файл з даними: ")
    info_file = input("Файл з інформацією: ")

    with open(info_file, "rb") as file:
        data_info = pickle.load(file)

    with open(data_file, "rb") as result_file:
        for data in data_info:
            with open(data["filename"], "wb") as file:
                file.write(result_file.read(data["size"]))

def main():
    file_info = []
    while True:
        choice = input("Оберіть опцію: [1] Додати файл [2] Зберегти дані [3] Переглянути дані [4] Декодувати дані [q] Вийти: ").lower()
        if choice == '1':
            add_files(file_info)
        elif choice == '2':
            save_data(file_info)
        elif choice == '3':
            view_data(file_info)
        elif choice == '4':
            decode_data()
        elif choice == 'q':
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
