def linha():
    print('xx' * 25)
    
linha()
print('EXERCÍCIO 040!')
linha()

nota_1 = float(input('DIGITE A PRIMEIRA NOTA DO ALUNO: '))
linha()
nota_2 = float(input('DIGITE A SEGUNDA NOTA DO ALUNO: '))
linha()

media = (nota_1 + nota_2) / 2

if media >= 7.0:
    print(f'VOCÊ FOI APROVADO! SUA NOTA FOI {media:.1f}')
    exit()
    
elif media >= 5.0 and media <= 6.9:
    print(f'VOCÊ FICOU DE RECUPERAÇÃO! SUA NOTA FOI {media:.1f}')
    exit()
    
else:
    print(f'VOCÊ ESTÁ REPROVADO! SUA NOTA FOI {media:.1f}')
    exit()
