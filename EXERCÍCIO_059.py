def linha():
    print('=-' * 25)
    
linha()
print('EXERCÍCIO 59!')
linha()
nome_titulo = 'MENU DE OPÇÕES'
titulo = nome_titulo.center(30, '=')
print(titulo)
linha()

n1 = int(input('ESCOLHA UM NÚMERO: '))
linha()
n2 = int(input('ESCOLHA UM SEGUNDO NÚMERO: '))
linha()
opção = int(input('''ESCOLHA UMA DAS OPÇÕES: 
    [1] SOMAR
    [2] SUBTRAIR
    [3] MULTIPLICAR
    [4] DIVIDIR
    [5] MAIOR NÚMERO
    ?'''))
    
while opção == 1:
    print(f' A SOMA DOS SEUS NÚMEROS É {n1} + {n2} = {n1+n2}')
    n1 = int(input('ESCOLHA UM NÚMERO: '))
    linha()
    n2 = int(input('ESCOLHA UM SEGUNDO NÚMERO: '))
    linha()
    opção = int(input('''ESCOLHA UMA DAS OPÇÕES: 
    [1] SOMAR
    [2] SUBTRAIR
    [3] MULTIPLICAR
    [4] DIVIDIR
    [5] MAIOR NÚMERO
    ?'''))
    
    
while opção == 2:
    print(f'A SUBTRAÇÃO DOS SEUS NÚMEROS É {n1} - {n2} = {n1-n2}')
    n1 = int(input('ESCOLHA UM NÚMERO: '))
    linha()
    n2 = int(input('ESCOLHA UM SEGUNDO NÚMERO: '))
    linha()
    opção = int(input('''ESCOLHA UMA DAS OPÇÕES: 
    [1] SOMAR
    [2] SUBTRAIR
    [3] MULTIPLICAR
    [4] DIVIDIR
    [5] MAIOR NÚMERO
    ?'''))
    
    
while opção == 3:
    print(f'A MULTIPLICAÇÃO DOS SEUS NÚMEROS É {n1} x {n2} = {n1*n2}')
    n1 = int(input('ESCOLHA UM NÚMERO: '))
    linha()
    n2 = int(input('ESCOLHA UM SEGUNDO NÚMERO: '))
    linha()
    opção = int(input('''ESCOLHA UMA DAS OPÇÕES: 
    [1] SOMAR
    [2] SUBTRAIR
    [3] MULTIPLICAR
    [4] DIVIDIR
    [5] MAIOR NÚMERO
    ?'''))
    
    
while opção == 4:
    print(f'A DIVISÃO DOS SEUS NÚMEROS É {n1} / {n2} = {n1/n2}')
    n1 = int(input('ESCOLHA UM NÚMERO: '))
    linha()
    n2 = int(input('ESCOLHA UM SEGUNDO NÚMERO: '))
    linha()
    opção = int(input('''ESCOLHA UMA DAS OPÇÕES: 
    [1] SOMAR
    [2] SUBTRAIR
    [3] MULTIPLICAR
    [4] DIVIDIR
    [5] MAIOR NÚMERO
    ?'''))
    
while opção == 5:
    lista = [n1, n2]
    maior_lista = max(lista)
    print(f'O MAIOR ENTRE ESSES DOIS NÚMEROS É O {maior_lista} ')
    n1 = int(input('ESCOLHA UM NÚMERO: '))
    linha()
    n2 = int(input('ESCOLHA UM SEGUNDO NÚMERO: '))
    linha()
    opção = int(input('''ESCOLHA UMA DAS OPÇÕES: 
    [1] SOMAR
    [2] SUBTRAIR
    [3] MULTIPLICAR
    [4] DIVIDIR
    [5] MAIOR NÚMERO
    ?'''))
