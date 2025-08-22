# List Comprehenesion : [expression for item in iterable if condition]
list1 = [i for i in range(21)]
print("List 1 : ", list1)
print("List 2 : ", list(i for i in list1 if i%2 == 1))