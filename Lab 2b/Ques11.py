with open("file.txt","r") as file:
    data = file.read()
    count = 0
    for i in data:
        if i != " " and i != "\n":
            count += 1
    print("Number of non-space characters: ", count)