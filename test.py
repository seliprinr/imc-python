peso = eval(input('Digite seu peso: '))
altura = eval(input('Digite sua altura: '))

imc = peso / altura ** 2

print(imc)

if imc < 18.5:
    print('Classificação: Magreza')
elif 18.5 <= imc < 25:
    print('Classificação: Normal')
elif 25 <= imc < 30:
    print('Classificação: Sobrepeso')
elif 30 <= imc < 40:
    print('Classificação: Obesidade')
else:
    print('Classificação: Obesidade Grave')


