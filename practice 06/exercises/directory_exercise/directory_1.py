import os
import shutil
os.makedirs("new_folder", exist_ok=True)
content = os.listdir("new_folder")
print(content)
for file in os.listdir("new_folder"):
    if file.endswith(".txt"):
        print(file)
os.makedirs("new_test_folder", exist_ok=True)
shutil.copy("new_folder/input.txt", "new_test_folder/input_backup.txt")