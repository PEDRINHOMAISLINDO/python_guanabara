import random # importando a biblioteca random
def linha():#criando uma função para criar uma linha
    print('=-' * 25)

nome = 'PEDRA X PAPEL X TESOURA'
nome_titulo = nome.center(50, '=')#center - método para colocar o nome(variável) no centro de uma string
    
print('EXERCÍCIO 045!')
linha()
print(nome_titulo)
linha()

escolha = str(input('''ESCOLHA UMA DAS 3 OPÇÕES:
    [1]PEDRA
    [2]PAPEL
    [3]TESOURA
    
    ? ''')).upper().strip()

computador = ['PEDRA', 'PAPEL', 'TESOURA']#criando uma lista
escolha_cpu = random.choice(computador)# choice - retorna um valor aleatório de uma lista. 

if escolha == '1' and escolha_cpu == 'PAPEL':
    print(f'VOCÊ PERDEU! A MÁQUINA ESCOLHEU {escolha_cpu}')
    exit()
    
elif escolha == '2' and escolha_cpu == 'TESOURA':
    print(f'VOCÊ PERDEU! A MÁQUINA ESCOLHEU {escolha_cpu}')
    exit()
    
elif escolha == '3' and escolha_cpu == 'PEDRA':
    print(f'VOCÊ PERDEU! A MÁQUINA ESCOLHEU {escolha_cpu}')
    exit()
    
elif escolha == escolha_cpu:
    print(f'NINGUÉM GANHOU! TODOS VOCÊS ESCOLHERAM {escolha}')
    exit()
    
else:
    print(f'VOCÊ GANHOU! A MÁQUINA ESCOLHEU {escolha_cpu}')
    exit()
