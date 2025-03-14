def linha():#CRIANDO UMA FUNÇÃO PARA CRIAR LINHAS
    print('=-' * 30)

nome_titulo = 'PRIMEIRAS LETRAS DE UM TEXTO'#CRIANDO UM TÍTULO CENTRALIZADO
titulo = nome_titulo.center(25, '=')

print('EXERCÍCIO 024!')
linha()
print(titulo)
linha()

cidade = str(input('DIGITE O NOME DA CIDADE EM QUE VOCÊ NASCEU: ')).strip().upper()
linha()
print(cidade[:5] == 'SANTO')

#UPPER() - DEIXA TODAS AS LETRAS EM MAIÚSCULAS
#STRIP() - DEIXA TODAS AS LETRAS EM MINÚSCULAS