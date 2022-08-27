import shutil
import os
from sys import argv

shutil.copyfile(argv[0], f'{argv[0]}0')
shutil.copyfile(argv[0], f'{argv[0]}1')
os.remove(argv[0])
