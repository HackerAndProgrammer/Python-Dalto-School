cadena1 = "HolaMaquinaSoyDalto"
cadena2 = "Welcome You Killing Machine"

#convierte a mayuscula

mayusc = cadena1.upper()

#convierte a minuscula

minusc = cadena1.lower()
                                                                                                                                                                    
#primera letra mayuscula

primera_letra_mayuscula = cadena1.capitalize()

#FIND
#buscamos una string en otra string, si no hay coincidencia, retorna -1, si la hay (retorna la posicion)

busqueda_find = cadena1.find("M")

#Index
#buscamos una cadena en otra cadena, si no hay coincidencia, nos retorna una excepcion, si la hay, nos retorna la posicion

#busqueda_index = cadena1.index("m")


#isnumeric
#si es numerico retorna True, si no, retorna False

is_numeric = cadena1.isnumeric()


#isalpha
#si es alfhanumerico retorna True, si no, el programa retorna False

is_alphanumeric = cadena1.isalpha()

#COUNT
##contamos las coincidencias de una cadena, dentro de otra cadena, el programa retorna la cantidad de veces que coincida, pero, si no hay coincidencia, el programa retorna 0

contar_coincidencia = cadena1.count("la Ma")

#LEN
#contamos cuantos caracteres tiene una string

contar_caracteres =  len(cadena1)

#startswith
#verificamos si una cadena empieza con otra cadena dada, si es asi, devuelve True

starts_with = cadena1.startswith("Hola")

#endswith
#verificamos si una cadena termina con otra cadena dada, si es asi, devuelve True

ends_with = cadena1.endswith("")

#replace
#si el valor 1 se encuentra en la string original, es reemplazada por el valor 2. Pero si no hay coincidencias, el programa retorna los valores originales

new_string = cadena1.replace(",", " ")

#Split
#separa strings con la nueva string que le establezcamos al programa, devolviendonos una matriz
separeted_string = cadena1.split("Maquina",)

print(is_alphanumeric)


