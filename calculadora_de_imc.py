print('Olá! Sou um programa desenvolvido para calcular IMC.\nInforme sua altura em metros e o peso em kg.\nNão use vírgulas comigo, coloque pontos no lugar.')
alt = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso/(alt**2)
print('Seu IMC é {:.2f}.'.format(imc))
if imc <= 18.5:
  print('Você está abaixo do peso.')
elif imc >= 18.5 or imc <= 24.9:
  print('Você está com peso normal (ou ideal).')
elif imc >= 25 or imc <= 29.9:
  print('Você está sobrepeso.')
elif imc >= 30 or imc <= 34.9:
  print('Você está com Obesidade (Grau I).')
elif imc >= 35 or imc <= 39.9:
  print('Você está com Obesidade severa (Grau II).')
elif imc >= 40:
  print('Você está com Obesidade mórbida (Grau III).')
