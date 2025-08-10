#También te hemos dicho que las cadenas de Python son inmutables. Esta es una característica muy importante. ¿Qué significa?
#Esto significa principalmente que la similitud de cadenas y listas es limitada. No todo lo que puede hacerse con una lista puede hacerse con una cadena.
#La primera diferencia importante no te permite usar la instrucción del para eliminar cualquier cosa de una cadena
#El ejemplo siguiente no funcionará:


alphabet = "abcdefghijklmnopqrstuvwxyz"
del alphabet[0]
 
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet.append("A")

##No pienses que la inmutabilidad de una cadena limita tu capacidad de operar con ellas.
##La única consecuencia es que debes recordarlo e implementar tu código de una manera ligeramente diferente: observa el código en el editor.

alphabet = "bcdefghijklmnopqrstuvwxy"

alphabet = "a" + alphabet
alphabet = alphabet + "z"

print(alphabet)


##Operaciones con cadenas: continuación

# Demonstración de min() - Ejemplo 1:
print(min("aAbByYzZ"))


# Demonstración de min() - Ejemplos 2 y 3:
t = 'Los Caballeros Que Dicen "Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))