import os
open(("desafios/"+__file__.split('\\')[-1]).split(".py")[0]+"-copia1.py", "w")
open(("desafios/"+__file__.split('\\')[-1]).split(".py")[0]+"-copia2.py", "w")
f1 = open(("desafios/"+__file__.split('\\')[-1]).split(".py")[0]+"-copia1.py", "a")
f2 = open(("desafios/"+__file__.split('\\')[-1]).split(".py")[0]+"-copia2.py", "a")
f1.write("".join((open(__file__)).readlines()))
f2.write("".join((open(__file__)).readlines()))
os.remove(__file__)