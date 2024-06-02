# 1 На створення змінних

# Варіант 1

name = "Іван Ковбель"
office = 365
weight = 79.5
height = 170.5

print(f"""Ім'я: {name}
Офіс: {office}
Вага: {weight}
Зріст: {height}""")

# Варіант 2

firs_name = input("Введіть своє прізвище: ").capitalize()
last_name = input("Введіть своє ім'я: ").capitalize()
office = input("Введіть номер офісу: ")
weight = input("Введіть свою вагу: ")
height = input("Введіть свій зріст: ")

print(f"""ПІБ: {firs_name} {last_name}
Офіс: {office}
Вага: {weight}
Зріст: {height}""")

# 2 на введення даних і особливості виводу

'text = input("Введіть текст: ")
choice = input("Виберіть 1 для великих літер або 2 для малих літер: ")
if choice == "1":
    print(text.upper())
elif choice == "2":
    print(text.lower())
else:
    print("Некоректний вибір")
