def wrap(fname, len):
    file = open(fname, 'r')
    data = file.read()
    file.close()
    print("Original file content:")
    print(data)
    file = open(fname, 'w')
    l = 0
    line = ""
    for i in data:
        if l == len:
            l = 0
            line +='\n'
            file.write(line)
            line = ""
        line += i
        l += 1
    file.close()
    file = open(fname, 'r')
    data = file.read()
    file.close()
    print(data)

print("Enter the name of the file to wrap:")
name = input()
print("Enter the length of each line:")
length = int(input())
wrap(name, length)