def linha():#função para criar uma linha
    print('xx' * 25)
    
linha()#chamando a função
print('EXERCÍCIO 043!')
linha()

#realizando perguntas e guardando as respostas em variáveis
peso = float(input('DIGITE SEU PESO: '))
linha()
altura = float(input('DIGITE SUA ALTURA: '))
linha()
 
 #realizando o calculo para descobrir o imc do usuário
imc = peso / (altura * altura)

#utilizando condições aninhadas em relação ao imc do usuário
if imc < 18.5:
    print(f'SEU IMC É {imc:.1f} VOCÊ ESTÁ ABAIXO DO PESO!')
    exit()
 
elif imc >= 18.5 and imc < 25:
    print(f'SEU IMC É {imc:.1f} VOCÊ ESTÁ NO PESO IDEAL!')
    exit()
    
elif imc >= 25 and imc < 30:
    print(f'SEU IMC É {imc:.1f} VOCÊ ESTÁ COM SOBREPESO!')
    exit()
    
elif imc >= 30 and imc < 40:
    print(f'SEU IMC É {imc:.1f} VOCÊ ESTÁ COM OBESIDADE!')
    exit()
    
elif imc > 40:
    print(f'SEU IMC É {imc:.1f} VOCÊ ESTÁ COM OBESIDADE MÓRBIDA')
    exit()
