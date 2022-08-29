import os


child1 = __file__[:-3]+"1.py"
child2 = __file__[:-3]+"2.py"
with open(__file__) as myself:
    lines = myself.readlines()

print("Dividing...")
with open(child1, "w") as child:
    child.writelines(lines)

with open(child2, "w") as child:
    child.writelines(lines)

print("Self destructing...")
os.remove(__file__)