with open("test.txt", "r") as file:
    data = file.readlines()
    for i in range(-1, -len(data)-1, -1):
        print(data[i])