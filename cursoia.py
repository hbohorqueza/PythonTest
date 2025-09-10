import datetime
nombre = input("Cuales tu apellido: ")
fecha= input("Formato de fecha aaaa/mm/dd: " )
hora = datetime.datetime.now().strftime("%H:%M")
print (f"hola, {nombre}")
print (f"la fecha ingresada es: {fecha} y la hora es {hora}" )

print ("la fecha ingresada es: " + fecha + " y la hora es " + hora )