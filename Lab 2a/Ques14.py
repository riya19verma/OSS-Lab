def triplet(n):
    list1 = []
    for i in range(1, n):
        sum = i + i + 1
        if sum <= n:
            list1.append([i, i + 1, sum])
    return list1

print("Enter a number: ")
n = int(input())
print("Triplets are:", triplet(n))