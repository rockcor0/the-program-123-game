# Receive from console or UI the commands to do something
class Command:

    def __new__(cls, *args, **kwargs):
        return super(Command, cls).__new__(cls)

    def __init__(self):
        print('Created Command')

    def __del__(self):
        pass

    # TODO character move foward
    def move_forward(self):
        return "Este lugar es algo extraño"

    # TODO character move back
    def move_back(self):
        return "Mejor retroceder. La mitad segura es la de atrás"

    # TODO character move to the left
    def move_left(self):
        return "Con la derecha escribo"

    # TODO character move to the right side
    def move_right(self):
        return "La mano cagada"

    # TODO character jump
    def jump(self):
        return "Allá vou"

    # TODO character take an object
    def take_an_object_from_floor(self):
        return "¿Será hoy mi día de suerte?"

    # TODO character take an object from bag
    def take_an_object_from_bag(self):
        pass

    # TODO character uses an object in the bag
    def use_an_object_from_bag(self):
        pass