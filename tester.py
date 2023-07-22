import os
file_name = "auto.txt"  # Replace "MyBook.txt" with the actual file name

# Get the absolute path of the file
file_path = os.path.abspath(file_name)

# Get the directory of the file
file_directory = os.path.dirname(file_path)

# Print the directory of the file
print("The directory of the file is:", file_directory)
