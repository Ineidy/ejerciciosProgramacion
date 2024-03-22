num1 = int(input("ingrese el dividendo: "))
num2 = int(input("Ingrese el divisor: "))

cociente= num1//num2
resto = num1 % num2

if resto == 0:
    print("La division es exacta.")
    print(f'cociente: {cociente}')
    print(f'Resto: {resto}')
else: 
    print("La division NO es exacta.")
    print(f'cociente: {cociente}')
    print(f'Resto: {resto}')
