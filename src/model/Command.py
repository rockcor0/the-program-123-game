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
        pass

    # TODO character move back
    def move_back(self):
        pass

    # TODO character move to the left
    def move_left(self):
        pass

    # TODO character move to the right side
    def move_right(self):
        pass

    # TODO character jump
    def jump(self):
        pass

    # TODO character take an object
    def take_an_object_from_floor(self):
        pass

    # TODO character take an object from bag
    def take_an_object_from_bag(self):
        pass

    # TODO character uses an object in the bag
    def use_an_object_from_bag(self):
        pass