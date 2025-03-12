from random import shuffle #UMA FORMA DE IMPORTAR SOMENTE A FUNÇÃO SHUFFLE
print('xx' * 25)
print('EXERCÍCIO 20!')
print('xx' * 25)

nome1 = input('PRIMEIRO NOME: ')
nome2 = input('SEGUNDO NOME: ')
nome3 = input('TERCEIRO NOME: ')
nome4 = input('QUARTO NOME: ')

lista = [nome1, nome2, nome3, nome4]
shuffle(lista)#EMBARALHA ITENS DENTRO DE UMA LISTA
print(lista)