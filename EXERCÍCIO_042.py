def linha():
    print('xx' * 25)
    
linha()
print('EXERCÍCIO 042!')
linha()

lado_a = float(input('DIGITE O PRIMEIRO LADO DE UM TRIÂNGULO: '))
linha()
lado_b = float(input('DIGITE O SEGUNDO LADO DE UM TRIÂNGULO: '))
linha()
lado_c = float(input('DIGITE O TERCEIRO LADO DE UM TRIÂNGULO: '))
linha()

if lado_a == lado_b and lado_a == lado_c:
    print('O SEU TRIÂNGULO É UM EQUILÁTERO!')
    exit()
    
elif lado_a == lado_b or lado_a == lado_c or lado_c == lado_b:
    print('O SEU TRIÂNGULO É ISÓSCELES!')
    exit()
    
else:
    print('O SEU TRIÂNGULO É ESCALENO!')
    exit()
