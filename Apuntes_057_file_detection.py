# Python file detection

import os

# Relative file path = folder/test.txt
# Absolute file path = C:/Users/Frey/Desktop/test.txt

file_path = "D:/Coding/Python/test.txt"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print("That location doesn't exist")