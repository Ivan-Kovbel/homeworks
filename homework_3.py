data = [1, 2, 31, 23, 213, 213, 123, 1, 1, 1, 21, 2, 3, 231, 2321, 31, 31, 23, 13, 2, 23, 23, 2, 2321]
data2 = [3, 2, 4, 34, 5, 45, 6, 65, 756, 4, 56, 856, 756, 67, 856, 234, 54, 754, 235, 547, 34, 346, 455, 3, 54, 634, 434, 634, 5, 2345]

def remove_duplicates(lst):
    return list(set(lst))
def find_unique_elements(lst):
    return set(lst)
def find_intersection(lst1, lst2):
    return tuple(set(lst1) & set(lst2))

# Позбуваємось дублювання у списках
unique_data = remove_duplicates(data)
unique_data2 = remove_duplicates(data2)

# Знаходимо унікальні елементи
unique_elements_data = find_unique_elements(data)
unique_elements_data2 = find_unique_elements(data2)

# Знаходимо перетин між data і data2 та формуємоя  кортеж
intersection_tuple = find_intersection(data, data2)

print(f"Список 'data' без дублювання: {unique_data}")
print(f"Список 'data2' без дублювання: {unique_data2}")
print(f"Унікальні елементи у 'data': {unique_elements_data}")
print(f"Унікальні елементи у 'data2': {unique_elements_data2}")
print(f"Перетин між 'data' і 'data2' у вигляді кортежу: {intersection_tuple}")
