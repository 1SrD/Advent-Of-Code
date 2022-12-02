fichero = open("Calorias.txt")
lineas = fichero.read().splitlines()
lista = []
tresMayores = 0
c = 0

for i in lineas:
     if i != "":
          c += int(i)
          lista.append(c)
     else:
          c = 0

lista.sort(reverse=True)

for x in lista[0:3]:
     tresMayores += x

print("La suma de los tres mayores es: ",tresMayores)