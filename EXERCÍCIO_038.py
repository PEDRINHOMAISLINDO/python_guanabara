def linha():
    print('xx' * 25)
    
linha()
print('EXERCÍCIO 038!')
linha()

numero_1 = float(input('ESCOLHA UM NÚMERO: '))
linha()
numero_2 = float(input('ESCOLHA UM SEGUNDO NÚMERO: '))
linha()

if numero_1 > numero_2:
    print(f'O NÚMERO UM({numero_1:.1f}) É MAIOR QUE O SEGUNDO NÚMERO({numero_2:.1f})')
    exit()
    
elif numero_1 < numero_2:
    print(f'O NÚMERO UM({numero_1:.1f}) É MENOR QUE O SEGUNDO NÚMERO({numero_2:.1f})')
    exit()
    
else:
    print(f'OS DOIS NÚMEROS SÃO IGUAIS ({numero_1:.1f} e {numero_2:.1f})')
    exit()
    
exit()
