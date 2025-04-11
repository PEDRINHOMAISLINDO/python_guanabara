import datetime # IMPORTANDO A BIBLIOTÉCA DATETIME
ano_atual = datetime.datetime.now().year # PARA CONSEGUIR O ANO ATUAL

def linha():#CRIANDO UMA FUNÇÃO PARA CRIAR UMA LINHA
    print('=-' * 25)

nome_titulo = 'GRUPO DA MAIORIDADE!' #CRIANDO UM TITULO
titulo = nome_titulo.center(30, '=')#CENTRALIZANDO O TÍTULO

print('EXERCÍCIO 054!')
linha()#LINHA CRIADA(LINHA 1)
print(titulo)#TÍTULO CRIANDO(LINHA 5)
linha()
contagem = 0 # VARIÁVEL VAZIA

for c in range(0, 7): # O QUE ESTÁ INDENTADO EMBAIXO IRÁ SE REPITIR 7 VEZES
    lista = [] # CRIANDO UMA LISTA VAZIA
    ano = int(input('DIGITE SEU ANO DE NASCIMENTO: '))
    idade = ano_atual - ano # ANO ATUAL - ANO DE NASCIMENTO DO USUÁRIO
    lista.append(idade) # ARMAZENANDO A VARIÁVEL IDADE DENTRO DE UMA LISTA
    if idade >= 21: # SE IDADE FOR MAIOR OU IGUAL A 18
        contagem += 1 # ADICIONANDO +1 NA VARIÁVEL VAZIA
        
print(f'NO TOTAL, {contagem} PESSOAS SÃO MAIORIDADE ENQUANTO {7 - contagem} NÃO SÃO MAIORIDADE')
    
