list1 = [4, 5, 6, 4, 3, 2, 1, 2, 3, 5, 6, 4]
list1.sort()
i = 1
while(i < len(list1)-1):
    if(list1[i] == list1[i-1]):
        print(list1[i])
    while(i < len(list1)-1 and list1[i] == list1[i-1]):
        i+=1
    i += 1