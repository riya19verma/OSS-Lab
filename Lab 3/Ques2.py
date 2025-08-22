def valuesort(dict1):
    item = list(dict1.items())
    item.sort()
    list1 = []
    for i in item:
        list1.append(i[1])
    return list1

dict1 = {'b': 1, 'c': 2, 'a': 3,'e': 4,'d': 5}
print(valuesort(dict1))