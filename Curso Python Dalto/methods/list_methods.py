#list() funcion
#creando una lista con list()
lista = list(["hola", "Dalto", 24, True, False, 56, 23, "I'm a Technology genius"])

#LEN
#devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#append
#agregando un elemento a la lista

lista.append("You have been hacked")

#insert
#agregando un elemento a la lista con un indice especifico

lista.insert(7, "TOMA MAMA")

#extend
#agregando varios elementos a la lista

lista.extend([False,2030])

#pop
#eliminando un elemento de la lista ( por su indice (especifico))

lista.pop(3)#-1 para eliminar el ultimo elemento,y asi sucesivamente(-1,-2,-3...)

#remove
#removiendo un elemento de la lista por su valor, si el programa no encuentra nada, nos devuelve una excepcion.

lista.remove("TOMA MAMA")

#print(lista)
list = [0, 1, 2, 3]
print(list[3])
