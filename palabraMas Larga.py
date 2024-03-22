
palabra1 = input("Palabra 1: ")
palabra2 = input("Palabra 2: ")
con1 = len(palabra1)
con2 = len(palabra2)

if con1 > con2:
    dif1mayor = con1 -con2
    print(f'La palabra {palabra1} tiene {dif1mayor} letras de mas que {palabra2}')
elif con2 > con1:
    dif2mayor = con2 -con1
    print(f'La palabra {palabra2} tiene {dif2mayor} letras de mas que {palabra1}')
elif con1 == con2:
    print("Las palabras tienen el mismo largo")