details = {
    "Pari" : 21,
    "Jay" : 32,
    "Urvashi" : 20,
    "Vikram" : 23,
    "Rohan" : 34,
    "Aditi" : 25
}

#(A)
print("People above 30:")
for name,age in details.items():
    if age > 30:
        print(name)

#(B)
details["Lavanya"] = 31
print(details)

#(C)
print("All students : ")
for (name,age) in details.items():
    print(f"{name} is of age {age}")

#(D)
del details["Jay"]
print("After deleting Jay:")
print(details)

#(E)
print("average age is : ")
average = sum(details.values()) / len(details)
print(average)