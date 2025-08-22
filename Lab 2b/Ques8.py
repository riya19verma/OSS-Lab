with open("output.txt","r+") as f:
    print("Original File Data : ")
    data = f.read()
    print(data)
with open("output.txt","w+") as f:
    print("Updated File Data : ")
    f.write("Hi, I am currently pursuing my BTech from Jaypee.")
    f.seek(0)
    print(f.read())
