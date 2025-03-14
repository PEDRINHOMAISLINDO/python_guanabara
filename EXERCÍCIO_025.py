def linha():#CRIANDO UMA FUNÇÃO PARA CRIAR LINHAS
    print('=-' * 30)

nome_titulo = 'PROCURANDO UMA STRING DENTRO DE OUTRA'#CRIANDO UM TÍTULO CENTRALIZADO
titulo = nome_titulo.center(25, '=')

print('EXERCÍCIO 025!')
linha()
print(titulo)
linha()

nome = str(input('DIGITE SEU NOME COMPLETO: ')).upper().strip()
#UPPER() - DEIXA TODAS AS LETRAS EM MAIÚSCULAS
#STRIP() - DEIXA TODAS AS LETRAS EM MINÚSCULAS
print(f'SEU NOME POSSUI SILVA: {'SILVA' in nome}')
# IN - VERIFICA SE TEM A PALAVRA SILVA EM NOME
