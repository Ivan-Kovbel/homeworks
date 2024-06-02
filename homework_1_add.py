# Калькулятор Індексу маси тіла

height = float(input("Введіть свій зріст (у метрах): "))
weight = float(input("Введіть свою вагу (у кілограмах): "))
bmi = weight / (height ** 2)

print("Ваш ІМТ: {:.2f}".format(bmi))
if bmi < 18.5:
    print("Недостатня вага")
elif bmi < 25:
    print("Нормальна вага")
elif bmi < 30:
    print("Надмірна вага")
else:
    print("Вітаю, ви жирний!")

