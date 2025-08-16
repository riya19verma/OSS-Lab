file = open("Test.txt", "w+")
list1 = ["Hey there I am Riya\n","I am in my 3rd year of BTech\n","I am 20 year old\n","I am in computer science branch\n"]
file.writelines(list1)
file.write("Thank you")
file.close()
file = open("Test.txt")
data = file.read()
print("\nData using read():\n",data)
print("Data using readlines:\n")
file.seek(0)
lines = file.readlines()
for line in lines:
    print(line)
file.close()