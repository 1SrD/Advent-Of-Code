fichero = open("guia.txt")
lineas = fichero.read().splitlines()
puntosTu = 0
a = 1 #roca
b = 2 #papel
c = 3 #tijeras

x = a #roca
y = b #papel
z = c #tijeras

print(lineas)
for i in lineas:

    if i == "A X": # piedra x piedra
        puntosTu += 4

    elif i == "B Y": #papel x papel
        puntosTu += 5

    elif i == "C Z": #tijeras x tijeras
        puntosTu += 6

    elif i == "A Y": #piedra x papel
        puntosTu += 8

    elif i == "A Z": #piedra x tijeras
        puntosTu += 3

    elif i == "B X": #papel x piedra
        puntosTu += 1

    elif i == "B Z": #papel x tijeras
        puntosTu += 9

    elif i == "C X": #tijeras x piedra
        puntosTu += 7

    elif i == "C Y": #tijeras x papel
        puntosTu += 2

print(puntosTu)

