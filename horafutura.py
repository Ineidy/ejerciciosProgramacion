print("QUIERES SABER QUE HORA SERÁ EN X TIEMPO?")
t = int(input("Escribe que hora es: "))
print("")
h = int(input("Escribe las horas que quieres avanzar: "))
print("")
htot = (t + h) % 24

print(f"La hora despues de {h} horas es: {htot}")

