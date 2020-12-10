import switch as switch

from src.model.App import App
from src.model.Message import Message


class Controller(App):

    def __new__(cls, *args, **kwargs):
        return super(Controller, cls).__new__(cls)

    def __init__(self):

        # Temp Command list. Get it from DB
        self.__commands = [('caminar', 'walk', 1),
                         ('correr', 'run', 2),
                         ('saltar', 'jump', 3),
                         ('saludar', 'hello', 4),
                         ('', '', 5),
                         ('', '', 6),
                         ('', '', 7)
                         ]

        self.users = ['0', 'System', 'Scenary']

        print('Init de controller')

    def validate_command(self, command):
        # Search in local data base for command
        found = False
        the_commands = self.__commands

        for i in the_commands:
            if i[0] == command.lower() or i[1] == command.lower():
                found = True
                break

        return found

    def get_commands(self):
        pass

    def do_something(self, user, command):
        for item in self.__commands:
            print(command.lower())
            if item[0] == command.lower() or item[1] == command.lower():
                return super().play(user, item[2])
            else:
                continue

    def get_commands(self):
        return self.__commands


# Test
c = Controller()
#c.validate_command('caminar')
