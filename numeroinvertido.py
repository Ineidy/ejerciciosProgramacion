numero = input("Escribe un numero de tres digitos para invertir: ")
if  len(numero) != 3:
     print("Error, solo tres digitos")
     exit()
else: 
    numero_inv = str(numero)[::-1]
    print()
    print(f"El numero {numero}, invertido es {numero_inv}")