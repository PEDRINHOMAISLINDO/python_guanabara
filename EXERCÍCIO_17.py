print('Xx' * 25) 
print('EXERCÍCIO 17!')
print('Xx' * 25)

cateto_opos = float(input('DIGITE SEU CATETO OPOSTO: '))
cateto_adja = float(input('DIGITE SEU CATETO ADJACENTE: '))

calculo = (cateto_opos ** 2 + cateto_adja ** 2) ** (1/2)

print(f'SUA HIPOTENUSA DEU {calculo}')
