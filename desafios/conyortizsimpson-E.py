import os

# No tenía ni idea como se hacía esto así que stack for the win
# https://stackoverflow.com/questions/5137497/find-the-current-directory-and-files-directory

name = os.path.realpath(os.path.realpath(__file__)).split("/")[-1]
with open(name, 'r') as a:
    codigo = a.read()

mitosis = [name.split(".")[0] + "-mitosis" + str(n) + ".py" for n in [1, 2]]
for m in mitosis:
    with open(m, 'w') as archivo:
        archivo.write(codigo)
        
os.remove(name)
