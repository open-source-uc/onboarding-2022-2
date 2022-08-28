from rich import print
# Usé este https://www.seekpng.com/ipng/u2w7o0r5o0a9r5q8_kirby-kirby-pixel-art/ como referencia

cielo = u'[pale_turquoise1]\u2589[/pale_turquoise1]'
kirby = u'[orchid]\u2588[/orchid]'
borde = u'[black]\u2588[/black]'
brillo = u'[white]\u2588[/white]'
ojos = u'[blue]\u2588[/blue]'
color = u'[red3]\u2588[/red3]'

print(cielo*20)
print(cielo*4+borde*2+cielo+borde*5+cielo*8)
print(cielo*3+borde*1+kirby*2+borde+kirby*5+borde*2+cielo*6)
print(cielo*2+borde*1+kirby*2+borde+kirby*8+borde*1+cielo*5)
print(cielo*2+borde*1+kirby*4+brillo+kirby+brillo+kirby*5+borde+cielo*4)
print(cielo*2+borde*1+kirby*4+ojos+kirby+ojos+kirby*5+borde+cielo*4)
print(cielo*2+borde*1+kirby*4+ojos+kirby+ojos+kirby*6+borde+cielo*3)
print(cielo*2+borde*1+kirby*2+color*2+kirby*3+color*2+kirby*5+borde+cielo*2)
print(cielo*2+borde*1+kirby*14+borde+cielo*2)
print(cielo*3+borde*1+kirby*10+borde*3+cielo*3)
print(cielo*3+borde*1+kirby*9+borde+color*3+borde+cielo*2)
print(cielo*4+borde*1+kirby*7+borde+color*4+borde+cielo*2)
print(cielo*4+borde*2+kirby*6+borde+color*4+borde+cielo*2)
print(cielo*3+borde+color*2+borde*2+kirby*3+borde+color*4+borde+cielo*3)
print(cielo*2+borde+color*5+borde*5+color*2+borde+cielo*4)
print(cielo*3+borde*6+cielo*3+borde*3+cielo*5)
print(cielo*20)

print("Amo a Kirby, está subestimado")
