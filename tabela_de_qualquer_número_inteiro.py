#!/usr/bin/env python3
def times(num, vezes):
    if vezes < 10:
        print('{} x {:2} = {}'.format(num, vezes, num*vezes))
    else:
        print(f'{num} x {vezes} = {num*vezes}')
#
print('Olá! Sou um programa para calcular a tabuada de qualquer número inteiro que você inserir.')
num = int(input('Digite o número de sua escolha: '))
print('-'*15)
for i in range(11):
    times(num, i)
print('-'*15)
