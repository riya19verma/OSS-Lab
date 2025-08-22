def invertdict(dict1):
    keys = list(dict1.keys())
    values = list(dict1.values())
    inverted = {}
    for i in range(len(keys)):
        inverted[values[i]] = keys[i]
    return inverted

dict1 = {'a': 1, 'b': 2, 'c': 3}
inverted_dict = invertdict(dict1)
print(inverted_dict)