def linha(): # FUNÇÃO PARA CRIAR LINHAS
    print('=-' * 25)
    
nome_titulo = 'NÚMEROS PRIMOS'# CRIANDO UM TÍTULO CENTRALIZADO
titulo = nome_titulo.center(30, '=')

print('EXERCÍCIO 052!')
linha()# LINHA CRIADA(LINHA 1)
print(titulo)#TÍTULO CRIADO(LINHA 4)
linha()

numero = int(input('DIGITE UM NÚMERO: '))
contador = 0 #CRIANDO UM CONTADOR

for c in range(1, numero + 1):# ESTRUTURA DE REPETIÇÃO. IRÁ SE REPETIR 1 ATÉ NUMERO(VARIÁVEL) + 1
    if numero % c == 0:# SE O RESTO DA DIVISÃO = 0
        contador2 += 1 # PREENCHER COM MAIS 1 A VARIÁVEL(DE ACORDO COM A CONDIÇÃO ÁCIMA)

    print(c, end = ' ')# DEIXANDO O PRINT DO C EM HORIZONTAL. EX: 1 2 3 4 5...
if contador > 2:
    print(f'\nSEU NÚMERO FOI DIVIDIDO {contador} ELE NÃO É PRIMO')
    exit()
    
else:
    print(f'\nSEU NÚMERO FOI DIVIDIDO POR {contador}NÚMEROS ELE É PRIMO')
    exit()
