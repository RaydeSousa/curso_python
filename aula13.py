nome = 'Ray de Sousa'
altura = 1.80
peso = 65
imc = peso / (altura * altura)

# f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura'
print(linha_1)

linha_2 = f'pesa {peso} quilos'
print(linha_2)

linha_3 = f'seu IMC é: {imc:.2f}'
print(linha_3)