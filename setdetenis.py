juegosGanadosA=int(input("Juegos ganados por A: "))
juegosGanadosB=int(input("Juegos ganados por B: "))
diferencia= juegosGanadosB - juegosGanadosA

if diferencia<0:
    diferencia=-(diferencia)

if (juegosGanadosB - juegosGanadosA)>2 or (juegosGanadosA > 7 or juegosGanadosB > 7) or (juegosGanadosA == juegosGanadosB):
    print('resultado invalido')
elif (juegosGanadosB >= 6 or juegosGanadosA >= 6) and diferencia>=2 :
    if juegosGanadosA>juegosGanadosB:
        print("Ganada B")
    elif juegosGanadosB>juegosGanadosA:
        print("Ganado B")
    elif juegosGanadosB==6 and juegosGanadosA==6:
        print("Invalido")
else:
    print("Aun no ha terminado")