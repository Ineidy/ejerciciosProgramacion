caracter = input("ingrese un caracter: ")
if caracter.isalpha():
    if caracter.isupper():
        print("La letra es mayuscula")
    elif caracter.islower():
        print("La letra es minuscula")
elif caracter.isdigit():
    print("Es numero")
else:
    print("No es letra ni numero")