import os
import shutil
import sys
import glob

path = sys.argv[0]

matching_files = len(glob.glob("Mamunoz42-E*.py"))

first_duplicate = f"Mamunoz42-E({matching_files}).py"

while os.path.exists(first_duplicate):
    matching_files += 1
    first_duplicate = f"Mamunoz42-E({matching_files}).py"

second_duplicate = f"Mamunoz42-E({matching_files + 1}).py"

shutil.copy(path, first_duplicate)
shutil.copy(path, second_duplicate)

os.remove(path)
