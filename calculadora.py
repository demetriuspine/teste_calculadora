a = int(input('digite o primeiro valor'))
b = int(input('digite o segundo valor'))
operacao = input('Digite a operação (+ ou -): ')
if operacao == '+':
    resultado = a + b
elif operacao == '-':
    resultado = a - b
else:
    resultado = 'Operação inválida'
print(resultado)
