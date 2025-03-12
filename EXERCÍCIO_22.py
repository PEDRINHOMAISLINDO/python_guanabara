print('EXERCÍCIO 22!')
print('XX' * 25)
seu_nome = str(input('DIGITE SEU O NOME: '))
print('XX' * 25)

print('ANALISANDO SEU NOME:')
print(f'SEU NOME EM MAIÚSCULO {seu_nome.upper()}') #UPPER DEIXA TODAS AS LETRAS MAIÚSCULAS
print(f'SEU NOME EM MINÚSCULO {seu_nome.lower()}')#LOWER DEIXA TODAS AS LETRAS MINÚSCULAS
print(f'SEU NOME TEM {len(seu_nome.replace(' ', ''))} LETRAS')# REPLACE TROCA UMA PALAVRA POR OUTRA. LEN CONTA TODOS OS CARACTERES.
separador = seu_nome.split()# SPLIT TIRA TODOS OS ESPAÇOS DO INÍCIO E FINAL DE UMA STRING
print(f'SEU PRIMEIRO NOME É {separador[0]} E ELE TEM {len(separador[0])} LETRAS')

