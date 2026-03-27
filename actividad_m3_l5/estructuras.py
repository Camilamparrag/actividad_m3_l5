# 1. crear estructura

# lista, permite elementos repetidos y se puede modificar
lista = ["negro", "azul", "blanco"] 
print("lista: ", lista)

# tupla no se puede modificar 
tupla = (4, 5, 6) 
print("tupla: ", tupla)

# conjunto no permite elementos repetidos y no tiene orden
conjunto = {1, 2, 3} 
print("conjunto: ", conjunto)

# diccionario almacena datos en pares clave:valor
diccionario = {
    "Nombre":"Camila",
    "Edad" : 25,
    "Ciudad" : "Arica"
    }
print("diccionario: ", diccionario)

# 2. acceder a elementos

print("segundo elemento lista: ", lista[1])

print("nombre: ", diccionario["Nombre"])


# Los sets no tienen orden definido, por lo que no existe una posición como [0], [1], etc.
# Por eso no se puede acceder a sus elementos por índice como en listas o tuplas.


# 3. contar e iterar

#- contar

print("cantidad lista: ", len(lista))

print("cantidad tupla: ", len(tupla))

print("cantidad conjunto: ", len(conjunto))

print("cantidad diccionario: ", len(diccionario))

#- iterar

print("lista:")
for i in lista:
    print(i)


print("tupla:")
for i in tupla:
    print(i)


print("conjunto:")
for i in conjunto:
    print(i)


print("diccionario:")
for clave, valor in diccionario.items():
    print(clave, ":", valor)

# 4. modificar estructuras

lista.append("verde")
print(lista)

conjunto.add(4)
print(conjunto)

lista.remove("negro")
print(lista)

diccionario.update({"Pais" : "Chile"})
print(diccionario)


# tupla no se puede modificar, es inmutable

