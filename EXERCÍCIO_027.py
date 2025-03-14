def linha():#CRIANDO UMA FUNÇÃO PARA CRIAR LINHAS
    print('=-' * 30)

nome_titulo = 'PRIMEIRO E ULTIMO NOME DA PESSOA'#CRIANDO UM TÍTULO CENTRALIZADO
titulo = nome_titulo.center(25, '=')

print('EXERCÍCIO 027!')
linha()
print(titulo)
linha()

nome = str(input('DIGITE SEU NOME COMPLETO: '))
nome_separado = nome.split()
print('OLÁ, PRAZER EM TE CONHECER!')
print(f'SEU PRIMEIRO NOME É {nome_separado[0]}')
print(f'SEU ÚLTIMO NOME É {nome_separado[-1]}')
