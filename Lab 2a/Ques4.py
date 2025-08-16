def function(list1,size):
    for i in range(0,len(list1),size):
        print("Sub-list:", list1[i:i+size])
    return
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
function(list1, 3)