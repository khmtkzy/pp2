import shutil
import os
with open("text.txt", "r") as file:
    content = file.read()
    print(content)
with open("text.txt", "a") as file:
    file.write("\n\tAPPEND LINE 6")
shutil.copy("text.txt", "text_backup.txt")
os.remove("text.txt")