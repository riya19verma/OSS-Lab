def func(item):
    if(item % 2 == 0):
        return True
    return False

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original List:", list1)
list2 = list(filter(func, list1))
print("Filtered List:", list2)