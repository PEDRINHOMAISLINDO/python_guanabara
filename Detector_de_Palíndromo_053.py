def linha():#CRIANDO UMA FUNÇÃO PARA CRIAR UMA LINHA
    print('=-' * 25)

nome_titulo = 'DETECTOR DE PALÍNDROMO' #CRIANDO UM TITULO
titulo = nome_titulo.center(30, '=')#CENTRALIZANDO O TÍTULO

print('EXERCÍCIO 053!')
linha()#LINHA CRIADA(LINHA 1)
print(titulo)#TÍTULO CRIANDO(LINHA 5)
linha()#LINHA CRIADA(LINHA 1)

frase = str(input('DIGITE UMA FRASE QUALQUER: ')).lower().strip()# LOWER - DEIXA TODA A STRING EM MINÚSCULAS; STRIP - TIRA OS ESPAÇOS DO INÍCIO E FINAL DE UMA STR
linha()
palavra = frase.split()# SEPARA A FRASE EM UMA LISTA DECORRENTE AOS ESPAÇOS EX: PEDRO H = 'PEDRO', 'H'
juntar = ''.join(palavra)#JOIN - JUNTA TODOS OS ELEMENTOS DA LISTA DE ACORDO COM OS ESPAÇOS EX: PEDROH
inverso = ''# VARIÁVEL VAZIA

for c in range(len(juntar)-1, -1, -1): # LEN - CONTA QUANTOS CARACTÉRES POSSUI
    inverso += juntar[c]
print(inverso)

if inverso == juntar:
    print('SUA PALAVRA É UM PALÍNDROMO!')
    
else:
    print('SUA PALAVRA NÃO É UM PALÍNDROMO!')
