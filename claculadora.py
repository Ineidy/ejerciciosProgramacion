num1=int(input("Operando: "))
operacion=input("Operador (+ , - , * , /, **)")
num2=int(input("Operando: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
restante = num1 ** num2


if (operacion== ("+")):
    print(f'{num1} {operacion} {num2} = {suma}')
elif (operacion== ("-")):
    print(f'{num1} {operacion} {num2} = {resta}')
elif (operacion== ("*")):
    print(f'{num1} {operacion} {num2} = {multiplicacion}')
elif (operacion== ("/")):
    print(f'{num1} {operacion} {num2} = {division}')
elif (operacion== ("**")):
    print(f'{num1} {operacion} {num2} = {restante}')