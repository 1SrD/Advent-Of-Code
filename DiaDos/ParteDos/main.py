fichero = open("guia.txt")
lineas = fichero.read().splitlines()
puntosTu = 0
a = 1 #roca
b = 2 #papel
c = 3 #tijeras

x = a #Perdida
y = b #Empate
z = c #Ganar

print(lineas)
for i in lineas:

    if i == "A X": #Perdida
        puntosTu += 3

    elif i == "B Y": #Empate
        puntosTu += 5

    elif i == "C Z": #Ganar
        puntosTu += 7

    elif i == "A Y": #Empate
        puntosTu += 4

    elif i == "A Z": #Ganar
        puntosTu += 8

    elif i == "B X": #Perdida
        puntosTu += 1

    elif i == "B Z": #Ganar
        puntosTu += 9

    elif i == "C X": #Perdida
        puntosTu += 2

    elif i == "C Y": #Empate
        puntosTu += 6

print(puntosTu)
