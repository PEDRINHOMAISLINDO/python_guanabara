def linha():
    print('=-' * 25)
    
nome_titulo = 'LOJAS PEDRO'
titulo = nome_titulo.center(25,'=') # método para centralizar o nome_titulo
print('EXERCÍCIO 044!')
linha() # função para criar uma linha.(1)
print(titulo)
linha()
valor_produto = float(input('DIGITE O VALOR DO SEU PRODUTO: '))
linha()
modo_de_pagamento = str(input('''ESCOLHA UM MODO DE PAGAMENTO: 
    [1] Á VISTA DINHEIRO/CHEQUE
    [2] Á VISTA CARTÃO
    [3] 2X NO CARTÃO
    [4] 3X OU MAIS NO CARTÃO
    
    ? ''')).upper().strip() #upper - deixar toda str maiúscula / strip - tirar os espaços do início e no final de uma str
    
if modo_de_pagamento == '1':
    calculo = valor_produto - (valor_produto * 0.10) # valor do produto - o seus 10%
    print(f'VOCÊ GANHOU 10% DE DESCONTO! AGORA SUA COMPRA FICOU COM O VALOR DE {calculo:.2f}')
    exit()
    
elif modo_de_pagamento == '2':
    calculo = valor_produto - (valor_produto * 0.05) # valor - 5% do seu valor
    print(f'VOCÊ GANHOU 5% DE DESCONTO! AGORA SUA COMPRA FICOU COM O VALOR DE {calculo:.2f}')
    exit()
    
elif modo_de_pagamento == '3':
    print(f'SUA COMPRA FOI PARCELADA EM 2X DE {valor_produto / 2:.2f}')
    print('VOCÊ NÃO TEVE NENHUM DESCONTO!')
    exit()
    
    
elif modo_de_pagamento == '4':
    escolha = str(input('''DESEJA PARCELAR EM:
        [1] 3X NO CARTÃO
        [2] MAIS DE 3X
        
        ? '''))
    if escolha == '1':
        calculo = valor_produto + (valor_produto * 0.2)
        calculo2 = (valor_produto + valor_produto * 0.2) / 3#calcular o valor do produto + 20% / 3
        print(f'''SUA CONTA FOI PARCELADA EM 3X DE {calculo2:.2f}
ELA TEVE UM ACRÉSCIMO DE 20%! {valor_produto * 0.2:.2f}''')
        exit()
        
    elif escolha == '2':
        parcelas = float(input('EM QUANTAS VEZES VOCÊ DESEJA PARCELAR: '))
        calculo = valor_produto + (valor_produto * 0.2)
        calculo2 = (valor_produto + valor_produto * 0.2) / parcelas #calcular o valor do produto + 20% / pela variável(parcelas)
        print(f'''SUA COMPRA FOI PARCELADA EM {parcelas:.0f}X DE {calculo2:.2f}
VOCÊ RECEBEU UM ACRÉSCIMO DE 20%({valor_produto * 0.2:.2f}) NO VALOR DA SUA COMPRA''')
        exit()
