n : int = int(input("Ingrese la cantidad de números reales que va a introducir: ")) #Se le pide al usuario la cantidad de números reales que va a introducir a la lista
nLista = [] #Creamos una lista vacía
for i in range(n): #Aplicamos ciclo for en rango de n
    i: float = float(input("Ingrese los número reales que usted quiera: ")) #Se le pide al usuario que ingrese el número que quiera. Esto sucederá dependiendo del número de reales que va a ingresea, esto gracias al ciclo for
    nLista.append(i) #Cada vez ingresamos el valor introducido a la lista
print(nLista)

promedio = sum(nLista)/n #Para sacar el promedio usamos la sum() con la lista que creamos sobre n = el número de reales que se introdujeron en la lista
print("El promedio de los valores de la lista es igual a", promedio) #Imprimimos