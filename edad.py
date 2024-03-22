from time import localtime
t = localtime()
t.tm_mday
t.tm_mon
t.tm_year
cont = 1

print("Ingrese su fecha de nacimiento")
while cont ==1:
    dia=int(input("Dia: "))
    if dia>31 or dia<1 :
        break
    mes=int(input("Mes: "))
    if mes>12 or mes<1 :
        break
    año=int(input("Año: "))
    if año>t.tm_year:
        break
    cont=cont+1

edad=t.tm_year-año
edad=edad-1
if dia<t.tm_mday and mes<t.tm_mon :
    edad=edad+1
print(f'Usted tiene {edad} años')