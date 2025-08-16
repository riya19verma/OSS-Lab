with open("Test.txt") as file:
    data = file.readlines()
    for line in data:
        print(line[-1::-1])