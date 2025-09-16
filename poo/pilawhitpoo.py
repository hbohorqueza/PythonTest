class Stack:
    def __init__(self):
        print("!Hola¡")
    
stack_object = Stack()


class Stack2:
    def __init__(self):
        self.stack_list = []

stack_object = Stack2()
print(len(stack_object.stack_list))


##PARA ESCONDER LA PROPIEDAD SE AÑADE DOS GUINES BAJOS __

class Stack3:
    def __init__(self):
        self.__stack_list1 = []

stack_object1 = Stack3()
print(len(stack_object1.stack_list1))

###Cuando cualquier componente de la clase tiene un nombre que comienza con dos guiones bajos (__), 
# se vuelve privado, esto significa que solo se puede acceder desde dentro de la clase.