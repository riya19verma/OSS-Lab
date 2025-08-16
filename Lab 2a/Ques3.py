def duplicates(list1):
    list2 = []
    for i in list1:
        if list1.count(i) > 1 and i not in list2:
            list2.append(i)
    return list2

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
print("Number of duplicate elements in the list:", duplicates(list1))