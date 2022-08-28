#Referencia: https://pythonadventures.wordpress.com/2014/03/20/unicode-box-drawing-characters/
import sys
chars = {
    'a': '┌',
    'b': '┐',
    'c': '┘',
    'd': '└',
    'e': '─',
    'f': '│',
    'g': '┴',
    'h': '├',
    'i': '┬',
    'j': '┤',
    'k': '╷',
    'l': '┼',
}
 
logo = """
aeeb     aeeb
fabf     faec
fdcheiieejf aeeieeb
faejaljkkff fabfkkf
ff fffffffdejdcffff
dc dcdggggeegeegggc
"""
logo2 = """
aeeeeeb aeeeeeb aeb aeb aeeeeeb
f aeb f f aeeec f f f f f aeeec
f f f f f deeeb f f f f f f
f f f f deeeb f f f f f f f 
f dec f aeeec f f dec f f deeeb
deeeeec deeeeec deeeeec deeeeec


"""
 
def main():
    for c in logo2:
        if c in chars:
            sys.stdout.write(chars[c])
        else:
            sys.stdout.write(c)
 
if __name__ == "__main__":
    main()

