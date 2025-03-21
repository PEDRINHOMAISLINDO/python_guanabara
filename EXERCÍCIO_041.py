import datetime

def linha():
    print('xx' * 25)
    
linha()
print('EXERCÍCIO 041!')
linha()

nome = str(input('DIGITE O NOME DO ATLETA: ')).upper().strip()
linha()
ano_atleta = int(input('DIGITE O ANO DE NASCIMENTO DO ATLETA: '))
linha()

ano_atual = datetime.datetime.today().year # para obter o ano atual
idade_atleta = ano_atual - ano_atleta

if idade_atleta <= 9:
    print(f'O ATLETA {nome} POSSUI {idade_atleta} DE IDADE; ELE ESTÁ NA CATEGORIA MIRIM.')
    exit()
    
elif idade_atleta > 9 and idade_atleta <= 14:
    print(f'O ATLETA {nome} POSSUI {idade_atleta} ANOS DE IDADE; ELE ESTÁ NA CATEGORIA INFANTIL. ')
    exit()
    
elif idade_atleta > 14 and idade_atleta <= 19:
    print(f'O ATLETA {nome} POSSUI {idade_atleta} ANOS DE IDADE; ELE ESTÁ NA CATEGORIA JÚNIOR.')
    exit()
    
elif idade_atleta > 19 and idade_atleta <= 25:
    print(f'O ATLETA {nome} POSSUI {idade_atleta} ANOS DE IDADE; ELE ESTÁ NA CATEGORIA SÊNIOR')
    exit()
    
else:
    print(f'O ATLETA {nome} POSSUI {idade_atleta} ANOS DE IDADE; ELE ESTÁ NA CATEGORIA MASTER')
    exit()
