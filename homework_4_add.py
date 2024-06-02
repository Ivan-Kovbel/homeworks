def find_element(data, result):
    def search_in_structure(structure, path):
        for key, value in structure.items() if isinstance(structure, dict) else enumerate(structure):
            if value == result:
                print("Знайшли елемент")
                return path + [key] if isinstance(structure, dict) else path + [key]
            if isinstance(value, (dict, list)):
                found = search_in_structure(value, path + [key])
                if found:
                    return found
        return None

    return search_in_structure(data, [])

# Приклади використання зі списком та словником (умови ДЗ №2)
data = [{1:2,2:3,3:[4,5,6,7,{8:9,10:[3,2,1,[155]]}]}]
result = find_element(data, 155)
print(f"Шлях до елемента: {result}")

data_dict = {"1":"1","2":[1,2,3,4,5,6,7,8,9,10,[3,2,4,1,2,3,4],[3,2,4,3,5,4,{"1":1,"2":2,"3":{"result":[1,2,3,4,155]}},6,5,7,6,9],[1,3,2,4,3,5,4,6,5]]}
result_dict = find_element(data_dict, 155)
print(f"Шлях до елемента: {result_dict}")
