from random import choice # importando dessa forma não precisará colocar randon.choice(), somente choice()
print('xx' * 25)
print('EXERCÍCIO 19!')
print('xx' * 25)

nome1 = input('DIGITE O PRIMEIRO NOME')
nome2 = input('DIGITE O SEGUNDO NOME: ')
nome3 = input('DIGITE O TERCEIRO NOME: ')
nome4 = input('DIGITE O QUARTO NOME: ')

lista = [nome1, nome2, nome3, nome4]
choice(lista)# método que embaralha os itens dentro de uma lista
print(choice(lista))