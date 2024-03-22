while True:

    año = int(input("Ingrese un año: "))
    añobi = año%4==0 and (año != 0 or año%400==0)
    if añobi:
        print(f'{año} es bisiesto')
    else:
        print(f'{año} no es bisiesto')
