# gcc -nostdlib jpuc1143-E.s -o jpuc1143-E
# Funciona en Linux x86-64 (y posiblemente en pre-M1 Mac OS).
# Nota: a diferencia de la clásica versión en Bash :(){ :|:& };:
# esta versión es instantáneamente letal. Hay tres reinicios de pc como testigos.

.global _start
.section .text

_start:

loop:
mov $0x39,%eax
syscall
jmp loop
# Estrictamente no es lo que pide el enunciado, pero sigue el espiritú.

mov $0x3c,%eax
mov $0x0,%ebx
syscall
