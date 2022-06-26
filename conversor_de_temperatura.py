#!/usr/bin/env python3
def cToF(temp):
    return (temp*9/5)+3

def fToC(temp):
    return (temp-32)*5/9
print('Olá! Sou um programa para converter °C em °F e vice-versa!\nPs: troque a vírgula por um ponto.\n')
print('[1] - °C para °F\n[2] - °F para °C\n')
choice = int(input('> '))
if choice == 1 or choice == 2: pass
else: 
    print('\nEscolha inválida.')
    quit()

temp = float(input ('\nDigite aqui a temperatura que você desejar: '))
if choice == 1: print(f'\n{temp}°C equivale à {cToF(temp)}°F.')
elif choice == 2: print(f'\n{temp}°F equivale à {fToC(temp)}°C.')