import random # IMPORTANDO A BIBLIOTECA RANDOM

print('_=' * 25)# CRIANDO LINHAS
print('EXERCÍCIO 28! GUNANBARA!')
print('_=' * 25)

numero = int(input('ESCOLHA UM NÚMERO ENTRE 0 E 5: '))
computador = random.randint(1, 5) # RANDINT É UMA FUNÇÃO QUE GERA UM NÚMERO INTEIRO DENTRO DE UM INTERVALO.(NESSE CASO 1 ATÉ 5)

if numero == computador: # CONDIÇÃO : SE NUMERO == COMPUTADOR
    print(f'VOCÊ GANHOU, O SEU NÚMERO E O MEU FOI {computador}')
else:
    print(f'CHUPA! O MEU NÚMERO FOI {computador} E O SEU FOI {numero}')
    
exit()