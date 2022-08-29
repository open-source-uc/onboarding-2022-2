import os
with open(f"cell{hash('mitosis1')}.py", "w") as clone:
    with open(__file__, "r") as prime:
        prime_code = prime.readlines()
        for line in prime_code:
            clone.write(line)
with open(f"cell{hash('mitosis2')}.py", "w") as clone:
    with open(__file__, "r") as prime:
        prime_code = prime.readlines()
        for line in prime_code:
            clone.write(line)
os.remove(__file__)
