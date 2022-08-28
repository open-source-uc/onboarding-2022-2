from rich import print

cielo = u'[blue]\u2588[/blue]'
blanco = u'\u2588'
naranjo = u'[#E1680F]\u2588[/#E1680F]'
negro = u'[black]\u2589[/black]'
punta = u'\u25B2'

print('Dibujo no muy producido del cohete Artemis, a propósito del lanzamiento del lunes. Igual se parece un poquito...')
print(cielo*60)
print(cielo*29 + blanco + cielo*30)
print(cielo*29 + blanco + cielo*30)
print(cielo*28 + 3*blanco + cielo*29)
print(cielo*28 + 3*blanco + cielo*29)
print(cielo*28 + 3*blanco + cielo*29)
print(cielo*28 + 3*naranjo + cielo*29)
print(cielo*27 + 5*naranjo + cielo*28)
print(cielo*27 + 5*naranjo + cielo*28)
print(cielo*27 + 5*naranjo + cielo*28)
print(cielo*25 + 2*blanco + 5*naranjo + 2*blanco + cielo*26)
print(cielo*25 + 2*blanco + 5*naranjo + 2*blanco + cielo*26)
print(cielo*25 + 2*blanco + 5*naranjo + 2*blanco + cielo*26)
print(cielo*25 + 2*blanco + 5*naranjo + 2*blanco + cielo*26)
print(cielo*25 + 2*blanco + 5*naranjo + 2*blanco + cielo*26)
print(cielo*25 + 2*blanco + 5*blanco + 2*blanco + cielo*26)
print(cielo*25 + 2*blanco + 2*negro + cielo + 2*negro + 2*blanco + cielo*26)
print(20*cielo + 20*negro + 20*cielo)
