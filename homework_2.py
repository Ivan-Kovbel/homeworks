# 1 На знаходження елементів

# Знайти індекси елементу 155 у

data = [[1,2,3],
        [4,5,6],
        [6,7,8,[155]]]
print(data[2][3][0])

data2 = {'1':'1',
         '2':'2',
         '3':'3',
         '4':[{'5':'5','6':[155]}]}
print(data2['4'][0]['6'][0])

data3 = [{1:2,
          2:3,
          3:[4,5,6,7,{8:9,10:[3,2,1,[155]]}]}]
print(data3[0][3][4][10][3][0])


# Ускладнена

data4 = {"1":"1",
         "2":[1,2,3,4,5,6,7,8,9,10,
              [3,2,4,1,2,3,4],
              [3,2,4,3,5,4,
               {"1":1,
                "2":2,
                "3":{"result":[1,2,3,4,155]}},
               6,5,7,6,9],
              [1,3,2,4,3,5,4,6,5]]}

print(data4["2"][11][6]["3"]["result"][4])


# 2 Реалізувати структури (через словники)
# 1 Товар. ключі:назва,опис,ціна

products = []
кількість_товарів = int(input("Введіть кількість товарів: "))
for i in range(кількість_товарів):
    product = {"name": input("Введіть назву товару {}: ".format(i+1)),
               "description": input("Введіть опис товару {}: ".format(i+1)),
               "price": float(input("Введіть ціну товару {}: ".format(i+1)))}
    products.append(product)
print("Список товарів:")
for product in products:
    print(product)


# 2 Стаття ключі: заголовок,текст,опис

def get_article_details():
    title = input("Введіть заголовок статті: ")
    text = input("Введіть текст статті: ")
    description = input("Введіть опис статті: ")
    comments = input("Введіть коментарі (розділені комами): ").split(',')
        article = {"title": title,
               "text": text,
               "description": description,
               "comments": comments}
    return article
def main():
    articles = []
    кількість_статей = int(input("Введіть кількість статей: "))    
    for i in range(кількість_статей):
        print("\nВведіть інформацію для статті", i + 1)
        article = get_article_details()
        articles.append(article)        
    print("\nСписок статей:")
    for idx, article in enumerate(articles):
        print(f"\nСтаття {idx + 1}:")
        print("Заголовок:", article["title"])
        print("Текст:", article["text"])
        print("Опис:", article["description"])
        print("Коментарі:", ", ".join(article["comments"]))
if __name__ == "__main__":
    main()

#3 Працівник ключі: ім'я,посада,офіс, де Офіс це словник із ключами: місто,номер, тип (віддалений або офіційний)

employees = []
number_of_employees = int(input("Введіть кількість працівників: "))
for i in range(number_of_employees):
    print("\nВведіть дані для працівника", i+1)
    name = input("Введіть ім'я працівника: ")
    position = input("Введіть посаду працівника: ")
    office_type = input("Оберіть тип офісу (1 - віддалений, 2 - офіційний): ")
    while office_type not in ('1', '2'):
        office_type = input("Неправильний вибір. Оберіть тип офісу (1 - віддалений, 2 - офіційний): ")
    офіс = {"city": input("Введіть місто офісу: "),
            "number": input("Введіть номер офісу: "),
            "type": "віддалений" if office_type == '1' else "офіційний"}
    employee = {"ім'я": name,
                "посада": position,
                "офіс": office_type}
    employees.append(employee)
print("\nСписок працівників:")
for idx, employee in enumerate(employees, start=1):
    print(f"\nПрацівник {idx}:")
    print("Ім'я:", employee["ім'я"])
    print("Посада:", employee["посада"])
    print("Офіс:", employee["офіс"])








