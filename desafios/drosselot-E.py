import os
import sys
import shutil
import random

path = sys.argv[0]
print(path[len(path) - 3:])

if path[len(path) - 4:] != "E.py":
    dir_path = path[: len(path) - 22]
    print(dir_path)
else:
    dir_path = path[: len(path) - 14]

file = os.path.basename(path)
files_in_dir = os.listdir(dir_path)
i = 0
for filen in files_in_dir:
    if filen == ".keep":
        files_in_dir.pop(i)
    i+= 1
print(path)

if file == "drosselot-E.py":
    shutil.copy(path, path[:len(path)-len(file)] + "(G11) drosselot-EXX.py")
    shutil.copy(path, path[:len(path)-len(file)] + "(G12) drosselot-EYY.py")

else:
    gen1 = file[len(file) - 5:len(file) - 3][random.randint(0,1)]
    otro_file = files_in_dir[random.randint(0, len(files_in_dir) - 1)]
    gen2 = otro_file[len(otro_file) - 5:len(otro_file) - 3][random.randint(0,1)]

    
    shutil.copy(path,path[:len(path)-len(file)] + "(G" + str(int(file[2]) + 1) + str(int(file[3]) + 1) + ") drosselot-E" + gen1 + gen2 + ".py" )

    gen1 = file[len(file) - 5:len(file) - 3][random.randint(0,1)]
    otro_file = files_in_dir[random.randint(0, len(files_in_dir) - 1)]
    gen2 = otro_file[len(otro_file) - 5:len(otro_file) - 3][random.randint(0,1)]


    shutil.copy(path,path[:len(path)-len(file)] + "(G" + str(int(file[2]) + 1) + str(int(file[3]) + 2) + ") drosselot-E" + gen1 + gen2 + ".py" )

os.remove(path)