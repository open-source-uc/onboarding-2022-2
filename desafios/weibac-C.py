from codecs import decode  # Mira mama sin chr()

positions = [77, 105, 108, 97, 110, 32, 87, 101, 105, 98, 101, 108]
print(''.join([decode(bytearray(range(a, a + 1))) for a in positions]))
