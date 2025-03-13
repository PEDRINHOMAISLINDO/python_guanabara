def linha(): # CRIANDO UMA FUNÇÃO PARA CRIAR LINHAS
    print('=-' * 25)
    
nome_titulo = 'TABUADA V.2.0'
titulo = nome_titulo.center(30, '=') # CRIANDO UM TITULO E DEIXANDO ELE CENTRALIZADO

print('EXERCÍCIO 049!')
linha()
print(titulo)
linha()
numero = float(input('DIGITE UM NÚMERO: '))

for c in range(1, 11):
    print(f'{numero:.2f} x {c} = {numero * c:.2f}')
    
exit()
