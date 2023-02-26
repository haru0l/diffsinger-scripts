import os

# Define the directory path where the search for subfolders starts
dir_path = os.getcwd()

# Loop through all subfolders within the parent directory
for root, dirs, files in os.walk(dir_path):
    for file in files:
        # Check if the file extension is .mid
        if file.endswith(".mid"):
            # If the file extension is .mid, delete the file
            os.remove(os.path.join(root, file))