import time # IMPORTANDO A BIBLIOTECA TIME

def linha(): # CRIANDO UMA FUNÇÃO PARA CRIAR LINHAS
    print('=-' * 25)
    
nome_titulo = 'CONTAGEM REGRESSIVA'
titulo = nome_titulo.center(30, '=') # CRIANDO UM TITULO E DEIXANDO ELE CENTRALIZADO

print('EXERCÍCIO 046!')
linha()
print(titulo)
linha()

for c in range(10, 1, -1): # FAZENDO A ESTRUTURA DE REPETIÇÃO CONTAR DE 10 ATÉ 1
    print(c)
    time.sleep(1)#CRIANDO UM INTERVALO DE 1 SEGUNDO.
print('FELIZ ANO NOVO MEUS AMORES!')
exit()
