print("Enter a list : ")
list1 = list(eval(input()))
print(list(filter(lambda x: x%2 == 0, list1)))
