f = open("demofile.txt")
print(f.read())

f = open("D:\\myfiles\welcome.txt")
print(f.read())

with open("demofile.txt") as f:
    print(f.read())

#CLOSE FILES
f = open("demofile.txt")
print(f.readline())
f.close()

#Read Only Parts of the File
with open("demofile.txt") as f:
    print(f.read(5))

#Read Lines
with open("demofile.txt") as f:
    print(f.readline())

with open("demofile.txt") as f:
    print(f.readline())
    print(f.readline())

with open("demofile.txt") as f:
    for x in f:
        print(x)