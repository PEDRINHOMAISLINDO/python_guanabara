import math
print('xx' * 25)
print('EXERCÍCIO 18!')
print('xx' * 25)

angulo = float(input('DIGITE SEU ANGULO: '))
seno = math.sin(math.radians(angulo))
Cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'O SEU SENO É {seno}')
print(f'O SEU COSSENO É {Cosseno}')
print(f'A SUA TANGENTE É {tangente}')