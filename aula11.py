# Uma introdução às f-strings (formatação de strings)

nome = 'Yago Fogaça'
altura = 1.80
peso = 54
imc = peso / altura ** 2

linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso:.2f} quilos e seu imc é {imc:.2f}'

print(linha_1)
print(linha_2)
