numer = float(input("Numerador: "))
denomi = float(input("Denominador: "))
try:
  resul = numer/denomi
except ZeroDivisionError as erro:
  print('Resultado: https://youtu.be/dQw4w9WgXcQ')
if denomi != 0:
  print("Resultado: {}".format(resul))
