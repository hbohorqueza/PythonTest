#Indexación
#Ya dijimos antes que las cadenas de Python son secuencias. Es hora de mostrarte lo que significa realmente.
#Las cadenas no son listas, pero pueden ser tratadas como tal en muchos casos.
#Por ejemplo, si deseas acceder a cualquiera de los caracteres de una cadena, puedes hacerlo usando indexación. Ejecuta el programa


the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

print()

#Interación
#El iterar a través de las cadenas funciona también. Observa el siguiente ejemplo:

the_string = 'silly walks'

for character in the_string:
    print(character, end=' ')

print()

### REBANADAS ##

alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])

### IN and NOT IN  #####


alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet)

alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" not in alphabet)
print("F" not in alphabet)
print("1" not in alphabet)
print("ghi" not in alphabet)
print("Xyz" not in alphabet)