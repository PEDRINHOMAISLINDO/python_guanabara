def linha(): #CRIANDO UMA FUNÇÃO PARA CRIAR LINHAS
    print('=-' * 25)

linha() # LINHA 1   
nome_titulo = 'EXERCÍCIO 57!'
titulo = nome_titulo.center(25, '=') # CENTER = COLOCO A VARIÁVEL NO CENTRO COM BASE NOS PARÂMETROS IMPOSTOS( (25, '=') )
linha()
print(titulo)
linha()
print('VALIDAÇÃO DE DADOS')
linha()

sexo = str(input('DIGITE SEU SEXO: ')).strip().upper() # STRIP = RETIRA ESPAÇOS NO INICIL E FIM DE UMA STRING. UPPER = LETRAS MAIÚSCULAS.

while sexo != 'MASCULINO' and sexo != 'FEMININO': # WHILE = VERIFICANDO SE SEXO(VAR) É DIFERENDE DE MASCULINO OU FEMININO
    print('DIGITE SEU SEXO NOVAMENTE!')
    sexo = str(input('DIGITE SEU SEXO: ')).strip().upper()
    
print('SEU GÊNERO FOI CONFIRMADO NO SISTEMA...')
exit()
