import datetime
def linha():
    print('xx' * 25)
    
linha()
print('EXERCÍCIO 039!')
linha()
ano_usuario = int(input('DIGITE O SEU ANO DE NASCIMENTO: '))
ano_atual = datetime.datetime.today().year
calculo = ano_atual - ano_usuario
linha()

if calculo > 18:
    print(f'VOCÊ JÁ TEM {calculo} ANOS. JÁ DEVERIA TER SE ALISTADO EM {ano_usuario + 18} .')
    exit()
    
elif calculo < 18:
    print(f'VOCÊ TEM SOMENTE {calculo}ANOS. VAI SE ALISTAR NO ANO DE {ano_usuario + 18} . ')
    exit()
    
else:
    print(f'VOCÊ JÁ POSSUI {calculo}! VAI SE ALISTAR AGORA EM {ano_usuario + 18} .')
    exit()
