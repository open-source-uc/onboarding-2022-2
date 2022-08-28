
def suma(num1, num2):
    aux = 0
    with open("recursion_aux.txt", "a") as file:
        file.write(f"{num1} + {num2}\n")
    try:
        with open("hora_de_sumar.txt", "r+") as file:
            for i in range(num1, num2):
                file.write(str(i))
                file.write(",")
    except FileNotFoundError:
        with open("hora_de_sumar.txt", "w") as file:
            for i in range(num1, num2 + 1):
                file.write(str(i))
                file.write(",")
    finally:
        with open("hora_de_sumar.txt", "r") as file:
            line = file.readlines()
            line = line[0].split(",")
    for i in line:
        aux += 1
    line.append(aux)
    while len(line) > 2:
        line.pop(1)
    try:
        if not line[0] != str(num1):
            if num1 > num2:
                suma(num1 - 1, num2)
            elif num2 > num1:
                suma(num1, num2 - 1)
        xd = (num1 - num2) if (num1 > num2) else (num2 - num1)
        if xd > 900:
            with open("recursion_aux.txt", "r") as file:
                rip_recursion = file.readlines()
                return eval(rip_recursion[0])
        return line[1]
    except RecursionError:
        with open("recursion_aux.txt", "r") as file:
            rip_recursion = file.readlines()
            return eval(rip_recursion[0])


if __name__ == "__main__":
    print(suma(0, 500))
