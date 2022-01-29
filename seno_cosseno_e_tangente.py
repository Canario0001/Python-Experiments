from math import sin, cos, tan, radians
angu = float(input('Digite um ângulo que você quiser: '))
seno = sin(radians(angu))
cosseno = cos(radians(angu))
tangente = tan(radians(angu))
print('O seno de {} é {:.2f}.'.format(angu, seno))
print('O cosseno de {} é {:.2f}.'.format(angu, cosseno))
print('O tangente de {} é {:.2f}.'.format(angu, tangente))
