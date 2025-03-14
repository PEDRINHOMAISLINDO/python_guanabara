import time, math

escolha = str(input('''VOCÊ PREFERE: 
    [1] P.A COM NÚMEROS COM NÚMEROS DECIMAIS
    [2] P.A COM NÚMEROS INTEIROS 
    
    ? ''')).upper().strip()
    
if escolha == '1':
    print('ABRINDO OUTRO PROGRAMA...')
    time.sleep(3)
    def linha(): # CRIANDO UMA FUNÇÃO PARA CRIAR LINHAS
        print('=-' * 25)
        
    nome_titulo = 'PROGRESSÃO ARITMÉTICA COM DECIMAIS'
    titulo = nome_titulo.center(30, '=') # CRIANDO UM TITULO E DEIXANDO ELE CENTRALIZADO
    
    print('EXERCÍCIO 051!')
    linha()
    print(titulo)
    linha()
    razao = float(input('DIGITE A RAZÃO DE SUA PA: '))
    linha()
    primeiro_termo = float(input('DIGITE O PRIMEIRO TERMO DE SUA PA: '))
    linha()
    print(primeiro_termo)
    for c in range(1, 10):
        print(f'{primeiro_termo + razao * c:.3f}')
    
elif escolha == '2':
     print('ABRINDO OUTRO PROGRAMA...')
     time.sleep(3)
     def linha(): # CRIANDO UMA FUNÇÃO PARA CRIAR LINHAS
        print('=-' * 25)
        
     nome_titulo = 'PROGRESSÃO ARITMÉTICA'
     titulo = nome_titulo.center(30, '=') # CRIANDO UM TITULO E DEIXANDO ELE CENTRALIZADO
    
     print('EXERCÍCIO 051!')
     linha()
     print(titulo)
     linha()
     razao = int(input('DIGITE A RAZÃO DE SUA PA: '))
     linha()
     primeiro_termo = int(input('DIGITE O PRIMEIRO TERMO DE SUA PA: '))
     linha()
    
     for c in range(primeiro_termo, primeiro_termo * 11, razao):
        print(c)
     exit()
    
