def linha():
    print('xx' * 25)
    
linha()
print('EXERCÍCIO 035!')
linha()

#criando uma forma para não manter espaços no salário. 9 até 11
salario_sujo = str(input('DIGITE O SEU SALÁRIO: '))
salario_limpo = salario_sujo.strip()
salario = float(salario_limpo)
linha()
#criando uma forma para não manter espaços no salário. 14 até 16
valorcasa_sujo = str(input('DIGITE O VALOR DA CASA: '))
valorcasa_limpo = valorcasa_sujo.strip()
valor_casa = float(valorcasa_limpo)
linha()
anos_meses = str(input('VOCÊ IRÁ PAGAR EM MESES OU ANOS: ')).strip().upper()
# se a variável anos_meses for preenchido com uma str 'ANOS'
if anos_meses == 'ANOS':
    anos = int(input('IRÁ PAGAR EM QUANTOS ANO(S): '))
    prestacao = valor_casa / (anos * 12)
    
    if prestacao > salario * 0.30:
        print(f'EMPRÉSTIMO NEGADO!!! O VALOR DA PRESTAÇÃO EXCEDEU OS 30%({prestacao:.2f}).')
        exit()
    else:
        print(f'EMPRÉSTIMO APROVADO!!! O VALOR DA PRESTAÇÃO NÃO EXCEDEU OS 30%({prestacao:.2f})')
        exit()
# se a variável anos_meses for preenchido com uma str 'MESES'
elif anos_meses == 'MESES':
    meses = int(input('IRÁ PAGAR EM QUANTOS MÊS(ES): '))
    prestacao = valor_casa / meses
     
    # Se prestação for maior que 30% do salário
    if prestacao > salario * 0.30:
        print(f'EMPRÉSTIMO NEGADO!!! O VALOR DA PRESTAÇÃO EXCEDEU OS 30%({prestacao:.2f}).')
        exit()
    else:
        print(f'EMPRÉSTIMO APROVADO!!! O VALOR DA PRESTAÇÃO NÃO EXCEDEU OS 30%({prestacao:.2f})')
        exit()
exit()
