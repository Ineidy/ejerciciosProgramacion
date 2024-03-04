import math
print("VAMOS A HAYAR LA HIPOTENUSA DE TU TRIANGULO! XD")
a = float(input("Escribe cuanto mide el cateto opuesto de tu triangulo: "))
b = float(input("Escribe cuanto mide el cateto adyacente de tu triangulo: "))

h = (a**2 + b**2)
h2 = math.sqrt(h)


print(f"LA HIPOTENUSA DE TU TRIANGULO CON UN CATETO OPUESTO DE {a}, Y UN CATETO ADYACENTE DE {b}, ES:  {h2}")
