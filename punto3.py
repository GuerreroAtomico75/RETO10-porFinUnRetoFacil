#Le pedimos al usuario que ingrese el número de elementos que quiere ingresar a la lista
n : int = int(input("Introduzca el número de enteros que va a incluir en la lista: "))
lista = []
#Hacemos un ciclo for, el cual mientras funcione se estarán ingresando números a la lista
for i in range(n):
    numero : float = float(input("Ingrese los números que usted quiera: "))
    lista.append(numero)
#Ordenamos la lista
lista.sort()
print(lista)
#Imprimos la lista al revés, para que los 0, queden al final.
lista.sort(reverse=True)
print(lista)