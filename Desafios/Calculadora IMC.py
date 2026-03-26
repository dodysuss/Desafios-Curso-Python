altura = float(input('Qual é a sua altura em cm? '))
peso = float(input('Qual é o seu peso em kg? '))
imc = peso / (altura / 100) ** 2
print(f'Seu IMC é {imc:.2f}')

if imc < 18.5:
    print('Você está abaixo do peso ideal.')
if imc > 18.5 and imc < 24.9:
    print('Você está com o peso ideal.')
if imc > 25.00 and imc < 29.9:
    print('Você está com sobrepeso.')
if imc > 30.00 and imc < 39.9:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade grave.')