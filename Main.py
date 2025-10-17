import os

def Arrage_file(all_file):
  for item in all_file:
    # Check if the current item is a file (skip folders)
    if os.path.isfile(item):

      # Skip the main Python script itself
      if item == 'Main.py':
        continue

      # Extract the file extension (e.g., "txt", "py", "jpg")
      ext = item.split(".")[1]

      # If a folder for this extension doesn't exist, create one
      # 'not' reverses the condition: it becomes True only if the folder does not exist
      if not os.path.exists(ext):
        os.makedirs(ext)

      # Create the destination path: e.g., "txt/example.txt"
      destination = os.path.join(ext, item)

      # Move (rename) the file into the corresponding extension folder
      os.rename(item, destination)

# Get a list of all files and folders in the current directory
all_file = os.listdir()

# Uncomment one of the following as needed:
Arrage_file(all_file)   # To organize files by extension

