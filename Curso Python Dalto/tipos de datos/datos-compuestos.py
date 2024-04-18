
#creando una lista los datos almacenados en esa variable( se pueden modificar )
lista = ["Lucas Dalto","Soy Dalto",True,1.85, "Soy Dalto"]

#creando una tupla los datos almacenados en esa variable ( no se pueden modificar )
tupla = ("Lucas Dalto","Soy Dalto",True,1.85, "Soy Dalto")

#esto es valido
lista[3] = "Maquinola"

#esto no es valido
#tupla[3] = "Maquinola"

#creando un conjunto (set) ( no se accede a elementos por su indice, no almacena datos duplicados)
conjunto = {"Lucas Dalto","Soy Dalto",True,1.85, "Soy Dalto"}

#print(conjunto[3]) -> no puede acceder al elemento

#creando un diccionario (dict) (la estructura es key : value y separamos con comas)
diccionario = {
    'nombre': "Lucas Dalto",
    'canal': "Soy Dalto",
    'esta emocionado': True,
    'altura': 1.85,
    'dato duplicado': "Soy Dalto"
}

print(diccionario['altura'] + 2)
