#5 students
names = ("Arushi", "Jay", "Parikshit", "Urvashi", "Vikram")

#(A)
print("Names of all the students:")
for name in names:
    print(name)
print(names)

#(B)
names = names + ("Rohan",)
print(names)

#(C)
ele = "Parikshit"
i = names.index(ele)
updated_names = names[:i] + names[i+1:]
print(updated_names)
names = updated_names

#(D)
print(names[1:4])

#(E)
print("If we try to modify an element we will face a TypeError")