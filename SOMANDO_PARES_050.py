def linha(): # CRIANDO UMA FUNÇÃO PARA CRIAR LINHAS
    print('=-' * 25)
    
nome_titulo = 'SOMANDO PARES'
titulo = nome_titulo.center(30, '=') # CRIANDO UM TITULO E DEIXANDO ELE CENTRALIZADO

print('EXERCÍCIO 050!')
linha()
print(titulo)
linha()

impares = 0 # CRIANDO VARIÁVEIS VAZIAS
pares = 0

for c in range(0, 6): # CRIANDO UMA REPETIÇÃO DE UM ATÉ SEIS.
    numero = int(input('DIGITE UM NÚMERO: ')) # IRÁ SE REPETIR SEIS VEZES.
    if numero % 2 == 0: # SE O RESTO DA DIVISÃO POR 2 == 0.
        pares += numero # ADICIONANDO VARIÁVEL NÚMERO NA VARIÁVEL CONTADOR.
        
    elif numero % 2 == 1: #  SE O RESTO DA DIVISÃO POR 2 == 1.
        impares += 1

print(f'VOCÊ COLOCOU {impares} NÚMEROS ÍMPARES. A SOMA DE TODOS OS NÚMEROS PARES É {pares}')
exit()
