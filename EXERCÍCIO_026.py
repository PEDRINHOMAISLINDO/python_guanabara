def linha():#CRIANDO UMA FUNÇÃO PARA CRIAR LINHAS
    print('=-' * 30)

nome_titulo = 'PROCURANDO UMA STRING DENTRO DE OUTRA'#CRIANDO UM TÍTULO CENTRALIZADO
titulo = nome_titulo.center(25, '=')

print('EXERCÍCIO 025!')
linha()
print(titulo)
linha()

frase = str(input('DIGITE UMA FRASE: ')).upper().strip()
print(f'A LETRA A APARECEU {frase.count('A')}')
print(f'A PRIMEIRA LETRA A APARECEU NA {frase.find('A') + 1}')
print(f'ELA APARECEU PELA ULTIMA VEZ NA {frase.rfind('A') + 1}')