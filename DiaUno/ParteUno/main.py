fichero = open("Calorias.txt")
lineas = fichero.read().splitlines()
lista = []
sumaDeTres = 0
c = 0

for i in lineas:
     if i != "":
          c += int(i)
          lista.append(c)
     else:
          c = 0

lista.sort(reverse=True)
print("El mayor de todos es: ",lista[0])
