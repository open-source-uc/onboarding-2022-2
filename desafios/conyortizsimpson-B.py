texto = "Buenos días buenas tardes x"

t = texto.swapcase().casefold().lower().upper().capitalize().center(0).title().strip("").zfill(0).rjust(10).ljust(10).rstrip().lstrip().expandtabs(2).replace("A", "A").translate({"x": "X"}).split(" ").copy().pop(2)
print(t)
