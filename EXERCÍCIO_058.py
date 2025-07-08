import random # IMPORTANDO A BIBLIOTECA RANDOM

print('_=' * 25)# CRIANDO LINHAS
print('EXERCÍCIO 28! GUNANBARA!')
print('_=' * 25)

numero = int(input('ESCOLHA UM NÚMERO ENTRE 0 E 10: '))
computador = random.randint(1, 10) # RANDINT É UMA FUNÇÃO QUE GERA UM NÚMERO INTEIRO DENTRO DE UM INTERVALO.(NESSE CASO 1 ATÉ 10)
contador = 0
while numero != computador:# while: ESTRUTURA DE REPETIÇÃO INFINITA. 
    numero = int(input('ESCOLHA IM NÚMERO ENTRE 0 E 10: '))
    contador += 1

if numero == computador: # CONDIÇÃO : SE NUMERO == COMPUTADOR
    print(f'VOCÊ GANHOU, O SEU NÚMERO E O MEU FOI {computador}')
    print(f'VOCÊ TENTOU {contador + 1} VEZES ATÉ ACERTAR!')
else:
    print(f'CHUPA! O MEU NÚMERO FOI {computador} E O SEU FOI {numero}')
    
exit()
