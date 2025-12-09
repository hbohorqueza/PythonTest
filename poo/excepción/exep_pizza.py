class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza


class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese


def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError(pizza, "no existe tal pizza en el menú")
    if cheese > 100:
        raise TooMuchCheeseError(pizza, cheese, "demasiado queso")
    print("¡Pizza lista!")

for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)
        
# Una de ellas es generada dentro de la función make_pizza() cuando ocurra cualquiera de estas dos situaciones erróneas: una solicitud de pizza incorrecta 
# o una solicitud de una pizza con demasiado queso.

# Nota:

# El remover el bloque que comienza con except TooMuchCheeseError hará que todas las excepciones que aparecen se clasifiquen como PizzaError.
# El remover el bloque que comienza con except PizzaError provocará que la excepción TooMuchCheeseError no pueda ser manejada, y hará que el programa finalice.

# La solución anterior, aunque elegante y eficiente, tiene una debilidad importante. Debido a la manera algo fácil de declarar los constructores, las nuevas 
# excepciones no se pueden usar tal cual, sin una lista completa de los argumentos requeridos.

# Eliminaremos esta debilidad estableciendo valores predeterminados para todos los parámetros del constructor. Observa:

class PizzaError(Exception):
    def __init__(self, pizza='desconocida', message=''):
        Exception.__init__(self, message)
        self.pizza = pizza
 
 
class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza='desconocida', cheese='>100', message=''):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese
 
 
def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError
    if cheese > 100:
        raise TooMuchCheeseError
    print("¡Pizza lista!")
 
 
for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)