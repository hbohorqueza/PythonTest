class TheSimplestClass:
    pass


mi_first_object = TheSimplestClass()


##CREAR UNA PILA

stack = []

def push(val):
    stack.append(val)


def pop():
    val = stack [-1]
    del stack[-1]
    return val

push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())