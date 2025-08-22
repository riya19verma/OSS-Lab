with open("file.txt","r") as f:
    data = f.readlines()
    for i in range(-1,-len(data)-1,-1):
        print(data[i].strip())