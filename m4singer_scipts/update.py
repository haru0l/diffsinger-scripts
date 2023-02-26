import os
import glob
from praatio import textgrid

# Set the directory path where the TextGrid files are located
directory_path = os.getcwd()

# Find all TextGrid files in the directory and its subdirectories
textgrid_files = glob.glob(os.path.join(directory_path, "**", "*.TextGrid"), recursive=True)

# Iterate over each TextGrid file and update it to the new format
for file_path in textgrid_files:
    tg = textgrid.openTextgrid(file_path, includeEmptyIntervals=False, duplicateNamesMode='rename')
    
    # Update the TextGrid file to the new format
    tg.save(file_path, format="long_textgrid", includeBlankSpaces=False)

    print(f"Updated {file_path} to the new TextGrid format.")