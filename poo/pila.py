class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

stack_object = Stack()

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())


##Tener tal clase abre nuevas posibilidades. Por ejemplo, ahora puedes hacer que más de una pila se comporte de la misma manera. 
# Cada pila tendrá su propia copia de datos privados, pero utilizará el mismo conjunto de métodos.
##Esto es exactamente lo que queremos para este ejemplo.
##Analiza el código:


stack_object_1 = Stack()
stack_object_2 = Stack()

stack_object_1.push(3)
stack_object_2.push(stack_object_1.pop())

print(stack_object_2.pop())


##############    Vamos a agregar una nueva clase para manejar pilas.   ###################


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

stack_objectHB = AddingStack()

for i in range(5):
    stack_objectHB.push(i)
print(stack_objectHB.get_sum())

for i in range(5):
    print(stack_objectHB.pop())