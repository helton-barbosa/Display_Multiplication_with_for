number = int(input('Entre com um número inteiro: '))
resultado = 0

for contador in range(1, 11):
    resultado = number * contador
    print(f'{number} x {contador} = {resultado}')
