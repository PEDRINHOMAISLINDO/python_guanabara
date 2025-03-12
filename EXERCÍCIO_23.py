print('EXERCÍCIO 23!')
print('Xx' * 25)

numero = int(input('DIGITE SEU NÚMERO: '))
print('Xx' * 25)
dezena = numero // 10 # // DIVISÃO INTEIRA
centena = numero // 100
unidade = numero % 10 # % RESTO DA DIVISÃO
unidade_milhar = numero // 1000
print(unidade)
print(dezena % 10)
print(centena % 10)
print(unidade_milhar)

# EX : NUMERO = 1234
# UNIDADE = NUMERO % 10 = 4
# DEZENA = NUMERO // 10 = 123 % 10 = 3
# CENTENA = NUMERO // 100 = 12 % 10 = 2
# UNIDADE_MILHAR = NUMERO // 1000 = 1