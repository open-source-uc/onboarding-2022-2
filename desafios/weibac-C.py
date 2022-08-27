from codecs import decode

positions = [77, 105, 108, 97, 110, 32, 87, 101, 105, 98, 101, 108]
bytes = [bytearray(range(a, a + 1)) for a in positions]
str_out = ''
for b in bytes:
    str_out += decode(b)
print(str_out)