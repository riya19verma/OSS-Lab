list1 = [3,2,5,1,3,5,7,8,9]
n = int(input("Enter a number: "))
if n > len(list1):
    print("Invalid input")
else:
    list1.sort()
    print(list1[-n::])