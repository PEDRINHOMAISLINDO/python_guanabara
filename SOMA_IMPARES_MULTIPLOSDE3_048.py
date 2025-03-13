def linha(): # CRIANDO UMA FUNÇÃO PARA CRIAR LINHAS
    print('=-' * 25)
    
nome_titulo = 'SOMA ÍMPARES MÚLTIPLOS DE TRÊS'
titulo = nome_titulo.center(30, '=') # CRIANDO UM TITULO E DEIXANDO ELE CENTRALIZADO

print('EXERCÍCIO 048!')
linha()
print(titulo)
linha()
lista = [] # CRIANDO UMA LISTA
for c in range(3, 500, 3): # FAZENDO UMA CONTAGEM DE 3 ATÉ 500 PULANDO DE 3 EM TRÊS EX.:3, 6, 9
    lista.append(c)# append : ADICIONA TODOS OS ITENS(NESTE CASO, OS NÚMEROS MÚLTIPLOS DE 3) DENTRO DE UMA LISTA.
    
print(f'A SOMA DE TODOS DARÁ {sum(lista)}')# SUM É UMA FUNÇÃO QUE SOMA TODOS OS ITENS DENTRO DE UMA LISTA.
exit()
