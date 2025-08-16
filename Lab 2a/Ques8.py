with open("Test.txt", "r") as file:
    data = file.read()
    lines = data.split("\n")
    word_count = 0
    for i in lines:
        word_count += len(i.split())
    print("Number of characters:", len(data))
    print("Number of lines:", len(lines))
    print("Number of words:", word_count)
    print("\nData:\n", data)