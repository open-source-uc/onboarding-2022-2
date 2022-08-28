a = "no habiamos visto un {temp1} tanto este año como este año tanto {temp2}"
print(a.capitalize().title().upper().lower().casefold().center(1).format(temp1="frio",temp2="calor").replace("calor","frio").split())

