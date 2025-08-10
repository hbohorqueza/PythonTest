##OPERTATIONS

##Concatenadas (unidas).
##Replicadas.

str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)


##Si deseas saber el valor del punto de código ASCII/UNICODE de un carácter específico, puedes usar la función ord() (proveniente de ordinal).

# Demostración de la función ord().

char_1 = 'a'
char_2 = ' '  # space

print(ord(char_1))
print(ord(char_2))

##Ahora asigna diferentes valores a ch1 y ch2, por ejemplo, α (letra griega alfa), y ę (una letra en el alfabeto polaco); luego ejecuta el código y ve qué resultado produce. Realiza tus propios experimentos.
##Si conoces el punto de código (número) y deseas obtener el carácter correspondiente, puedes usar la función llamada chr().
##La función toma un punto de código y devuelve su carácter.

# Demostración de la función chr().

print(chr(97))
print(chr(945))
