import os
os.remove("demofile.txt")

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")

#make a folder
os.mkdir("myfolder")
#remove an empty folder
os.rmdir("myfolder")