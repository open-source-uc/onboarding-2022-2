import shutil
import os
from sys import argv

name = argv[0].split('.')[0]
shutil.copyfile(argv[0], f'{name}0.py')
shutil.copyfile(argv[0], f'{name}1.py')

os.remove(argv[0])
