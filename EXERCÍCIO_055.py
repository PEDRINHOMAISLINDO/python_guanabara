def linha(): # FUNÇÃO PARA CRIAR LINHAS
    print('=-' * 25)
    
nome_titulo = 'EXERCÍCIO 055'
titulo = nome_titulo.center(25, '=')#CRIANDO UM TÍTULO

linha()
print(titulo)
linha()
lista = []# CRIANDO UMA LISTA

for c in range(1, 6):# CRIANDO UMA ESTRUTURA DE REPETIÇÃO. 1 ATÉ 5
    peso = float(input('DIGITE SEU PESO: '))#IRÁ SE REPETIR 5 VEZES
    lista.append(peso)#IRÁ SE REPETIR 5 VEZES
    
lista_ordem = sorted(lista, reverse=True)# MUDNADO A ORDEM DE UMA LISTA DEIXANDO ELA DO MAIOR PARA O MENOR.
print(f'O MAIOR PESO FOI DE {max(lista):.2f}Kg')#max: VER QUAL É O MAIOR ITEM DA LISTA
print(f'O MENOR PESO FOI DE {min(lista):.2f}Kg')#min: VER QUAL É O MENOR ITEM DA LISTA

print('A ORDEM DOS PESOS FICOU:')
print(lista_ordem)
